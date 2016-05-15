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
]
