from django import forms
from .models import ActivityRecord
from django.core.exceptions import ValidationError
from datetime import date

# ActivityRecord登録・編集用フォーム
class ActivityRecordForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': date.today().strftime('%Y-%m-%d')}))
    hours = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(24)]), initial=0)
    minutes = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(60)]), initial=0)

    class Meta:
        model = ActivityRecord
        fields = ['date', 'hours', 'minutes', 'memo']

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours')
        minutes = cleaned_data.get('minutes')
        activity_date = cleaned_data.get('date')


        # 確認: 選択された日付が未来のものでない
        if activity_date is not None and activity_date > date.today():
            raise ValidationError("未来の日付は選択できません。")

            # 確認:時間が入力されていない
        if hours == 0 and minutes == 0:
            raise ValidationError("時間を入力してください。")

        # 確認: 入力されたhours, minutesを分単位に変更
        if hours is not None and minutes is not None:
            cleaned_data['duration'] = hours * 60 + minutes

        return cleaned_data

    # hours, minutsを分単位に変換した後の値をdurationカラムに保存します
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.duration = self.cleaned_data['duration']

        if commit:
            instance.save()

        return instance
