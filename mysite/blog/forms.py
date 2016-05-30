from django import forms
from .models import Post

# use a ModelForm form, which saves the result of the form to a model
class PostForm(forms.ModelForm):

    # tell django which model backs this form, and which fields from that model.
    # in this case, we want control over the title and text; author will be the
    # logged-in person writing it, and created_date will be auto-generated.
    class Meta:
        model = Post
        fields = ('title', 'text',)
