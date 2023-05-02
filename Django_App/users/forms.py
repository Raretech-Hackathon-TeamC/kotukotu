from django import forms
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

# ユーザー登録用
class RegistForm(forms.ModelForm):
    user_name = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')
        # validate_passwordで画面遷移せずにエラーを表示
        validate_password(self.cleaned_data['password'], self.instance)
        
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


# login用
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())