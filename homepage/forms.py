from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    your_name = forms.CharField(max_length=100)

# class ArticleForm(ModelForm):
#     class meta:
#         model = Article
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class SignUpForm(forms.Form):
    # username = forms.CharField(
    #     required=True,
    #     label=u"用户名",
    #     error_messages={'required': '请输入用户名'},
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': u"用户名",
    #         }
    #     ),
    # )
    # password = forms.CharField(
    #     required=True,
    #     label=u"密码",
    #     error_messages={'required': u'请输入密码'},
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'placeholder': u"密码",
    #         }
    #     ),
    # )
    # def clean(self):
    #     if not self.is_valid():
    #         raise forms.ValidationError(u"用户名和密码为必填项")
    #     else:
    #         cleaned_data = super(SignUpForm, self).clean()
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField(max_length=120, required=True)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'uid', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pwd', 'placeholder': 'Password'}))