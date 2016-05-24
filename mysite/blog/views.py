from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Views are merely functions that are called when a valid request is received.
# If a requests's url matches a pattern-view pair in the urls.py file, the corresponding
# view function is executed.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
