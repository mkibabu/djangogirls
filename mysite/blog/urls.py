from django.conf.urls import url
from . import views

'''
This file did not exist; we create it to hold the urls specific to the 'blog'
app within the mysite project. This helps keep the mysite urls.py file cleaner,
and makes the blog application more encapsilated and easier to copy elsewhere.
'''

urlpatterns = [
    #url(r'pattern', view_to_handle_request, name='a name for the view')
    url(r'^$', views.post_list, name='post_list'),
    
    # here, match a url with the pattern 'post/NNN..', where NNN.. are digits.
    # the digits after the 'post/' are to be passed to the view as a variable 'post_id'.
    # pattern: starts with "post/", is followed by gte 1 digit(s) and ends.
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^post/new/$', views.post_new, name='post_new'),

    url(r'^post/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit')     
]

