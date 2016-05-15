from django.shortcuts import render

# Views are merely functions that are called when a valid request is received.
# If a requests's url matches a pattern-view pair in the urls.py file, the corresponding
# view function is executed.

def post_list(request):
    return render(request, 'blog/post_list.html')
