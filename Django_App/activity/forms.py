from django import forms
from .models import ActivityRecord
from datetime import date

# ActivityRecord登録・編集用フォーム
class ActivityRecordForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hours = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(24)]), initial=0)
    minutes = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(60)]), initial=0)

    class Meta:
        model = ActivityRecord
        fields = ['date', 'hours', 'minutes', 'memo']

    # hours, minutesに初期値を設定
    def __init__(self, *args, **kwargs):
        super(ActivityRecordForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['hours'], self.initial['minutes'] = divmod(self.instance.duration, 60)
            self.initial['date'] = self.instance.date.strftime('%Y-%m-%d')

    # hours, minutesを分単位に変換
    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours')
        minutes = cleaned_data.get('minutes')

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
