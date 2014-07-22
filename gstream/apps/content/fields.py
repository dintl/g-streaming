from taggit.forms import TagField as TaggitTagField

from .widgets import TagWidget

class TagField(TaggitTagField):
    widget = TagWidget