from django import forms

class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    