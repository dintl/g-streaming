from taggit.forms import TagWidget as TaggitTagWidget

class TagWidget(TaggitTagWidget):
    """
        Adds in bootstap tag input to tag widget
    """
    def render(self, name, value, attrs=None):
        if not attrs:
            attrs = {}
        attrs['data-role'] = "tagsinput"

        return super(TagWidget, self).render(name, value, attrs)

    class Media:
        js = ('content/bootstrap-tagsinput/bootstrap-tagsinput.min.js',)
        css = {'screen': ('content/bootstrap-tagsinput/bootstrap-tagsinput.css',),}
