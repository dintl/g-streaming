from django import forms

from gstream.apps.content.fields import TagField

class GLogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    tags = TagField()
    