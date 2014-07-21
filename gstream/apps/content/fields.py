from django import forms
from .widgets import TagWidget

class TagField(forms.CharField):
    widget = TagWidget