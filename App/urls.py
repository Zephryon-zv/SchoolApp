"""
URL configuration for iblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from . import views
from django.urls import re_path as url
from django.views.static import serve

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # path('home/', home)
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('error-404/', views.error_404, name='error-404'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    
    # Add more URL patterns for other pages/views as needed
]
