from django import forms
from .models import ActivityRecord
from django.core.exceptions import ValidationError
from datetime import date

# ActivityRecord登録・編集用フォーム
class ActivityRecordForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': date.today().strftime('%Y-%m-%d')}))
    duration = forms.IntegerField(widget=forms.TimeInput(attrs={'type': 'time', 'value': '00:00'}))

    class Meta:
        model = ActivityRecord
        fields = ['date', 'duration', 'memo']

    # date, durationの初期値を設定
    def __init__(self, *args, **kwargs):
        super(ActivityRecordForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['duration'] = f"{self.instance.duration // 60:02d}:{self.instance.duration % 60:02d}"
            self.initial['date'] = self.instance.date.strftime('%Y-%m-%d')

    # durationを分単位に変換
    def clean(self):
        cleaned_data = super().clean()
        duration = cleaned_data.get('duration')
        activity_date = cleaned_data.get('date')

        # 確認: 選択された日付が未来のものでない
        if activity_date is not None and activity_date > date.today():
            raise ValidationError("未来の日付は選択できません。")

        # 確認:時間が入力されていない
        if duration == 0:
            raise ValidationError("時間を入力してください。")

        return cleaned_data


    # 分単位に変換した後の値をdurationカラムに保存します
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.duration = self.cleaned_data['duration']

        if commit:
            instance.save()

        return instance
