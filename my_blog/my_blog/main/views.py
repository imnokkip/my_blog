from django.shortcuts import render, get_object_or_404
from .models import Post, Project, GalleryImage

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'main/detail.html', {'post': post})

def projects(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/projects.html', {'posts': posts})

def projects_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-created_at')
    print(projects)
    return render(request, 'main/projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, 'main/project_detail.html', {'project': project})

def gallery_view(request):
    images = GalleryImage.objects.all().order_by('-created_at')
    return render(request, 'main/gallery.html', {'images': images})