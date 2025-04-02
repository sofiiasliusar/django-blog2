from django import forms
from .models import ArticleImage


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:  # TODO ???
        model = ArticleImage
        fields = '__all__'  # TODO ???
