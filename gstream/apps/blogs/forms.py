from django import forms

from gstream.apps.content.fields import TagField

class BlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    tags = TagField()
    