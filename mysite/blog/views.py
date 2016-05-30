from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Views are merely functions that are called when a valid request is received.
# If a requests's url matches a pattern-view pair in the urls.py file, the corresponding
# view function is executed.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    '''
    Get the post details. The post_id variable must be named the exact same as the
    urls.py matching entry has it named.
    '''
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

