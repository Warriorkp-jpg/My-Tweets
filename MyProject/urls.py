"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from MyTweets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('', views.tweet_list, name='tweet_list'),  # Home page view
    path('create/', views.tweet_create, name='tweet_create'),
     path('MyTweets/', views.tweet_list, name='tweet_list'),
    path('<int:tweet_id>/delete/', views.tweet_del, name='tweet_del'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
]

# ✅ Correct way to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
