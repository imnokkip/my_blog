from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('projects/', views.projects_list, name='projects_list'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('music/', views.music_list, name='music'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)