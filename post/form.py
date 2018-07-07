from django.forms import ModelForm
from . models import Post
from django.forms import Textarea, ImageField


class CreatePost(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update({"class": "form-control-file",
                                                  "col": 100, "row": 2})
        self.fields["containt"].widget = Textarea()
        self.fields["containt"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Post
        fields = "__all__"
        # widgets = {'containt': {Textarea(attrs={'cols': 50, 'rows': 10})}}


class UpdatePost(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
