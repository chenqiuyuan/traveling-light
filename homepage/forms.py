from django import forms
from django.forms import ModelForm

class NameForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    your_name = forms.CharField(max_length=100)

# class ArticleForm(ModelForm):
#     class meta:
#         model = Article
class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()