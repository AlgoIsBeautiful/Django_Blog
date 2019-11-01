"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from blog import views
from django.conf.urls import url, include
from django.contrib import admin

# we want import that views2.py
# the path ('http://127.0.0.1:8000/****') to replace here
urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    # url(r'^search/', include('haystack.urls')),
]
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('', include('blog.urls'))
# ]
#
#     path('contact/', views.contact_view, name='contact'),
#     path('about/', views.about_view, name='about'),
#     path('', views.home_view, name='home'),
#     path('^admin/', admin.site.urls),
#     path('admin/blog/article/', views.articles, name='article'),
# ]
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('', include('blog.urls'))
