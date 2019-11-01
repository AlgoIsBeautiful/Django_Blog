from django.conf.urls import url

from . import views

# below app_name tells Django that this urls.py belongs to 'blog'
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]

    # [0-9]+ represents 1 or more digits /1/, /255/
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


