from django import forms
from .models import ArticleImage


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:  #  ??? generates fields based on a model (corresponds to)
        model = ArticleImage
        fields = '__all__'  #  ??? which fields should be included in the form.
