from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Views are merely functions that are called when a valid request is received.
# If a requests's url matches a pattern-view pair in the urls.py file, the corresponding
# view function is executed.

def post_list(request):
    '''
    Returns a list of all blog posts published any time before now, ordered by 
    date of publication.
    '''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    '''
    Get the post details. The post_id variable must be named the exact same as the
    urls.py matching entry has it named.  Returns a 404 page if no matching post
    is found
    '''
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    '''
    Two possible scenarios: we're hitting the page for the first time, in which
    case, request.POST is empty. Or we're submitting a form, in which case,
    request.POST has form data.
    '''
    if request.method == 'POST':
        # create a form with the POST data
        form = PostForm(request.POST)
        # check if all required fields are present, in the right format 
        if form.is_valid():
            # save the form as a post, don't write to db yet
            post = form.save(commit=False)
            # add an author and published_date to the post object
            post.author = request.user
            post.published_date = timezone.now()
            # persist the model to the db
            post.save()
            # redirect to post_detail page for this post
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, post_id):
    '''
    Edits a post that matches the given post_id, or 404s.
    '''
    # get the post matching this post_id
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # if we're submitting an edited post, create a form backed by the POST
        # data, as a repalcement for this instance.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


