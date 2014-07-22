from django import forms
from django_wysiwyg import clean_html

from gstream.apps.content.fields import TagField

from .models import GLog

class GLogForm(forms.ModelForm):
   
    tags = TagField()

    def clean_content(self):
        return clean_html(self.cleaned_data['content'])

    class Meta:
        model = GLog
        fields = ('title', 'content', 'tags')
