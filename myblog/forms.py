from django import forms

from .models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "This appear on the tab of your browser"}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'username', 'value': '', 'id': 'gokul',
                       'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class Editform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "This appear on the tab of your browser"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
