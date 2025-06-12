from django.contrib import admin
from .models import Post, Project, GalleryImage
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published', 'image_preview')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'author')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview'),
        }),
        ('Даты и публикация', {
            'fields': ('created_at', 'updated_at', 'is_published'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;"/>')
        return "Нет изображения"
    
    image_preview.short_description = "Превью"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('preview_image',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description')
        }),
        ('Медиа', {
            'fields': ('image', 'preview_image')
        }),
        ('Ссылки', {
            'fields': ('github_url', 'demo_url')
        }),
        ('Публикация', {
            'fields': ('is_published',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;"/>')
        return "Нет изображения"
    
    def github_link(self, obj):
        if obj.github_url:
            return mark_safe(f'<a href="{obj.github_url}" target="_blank">GitHub</a>')
        return "-"
    
    preview_image.short_description = "Превью"
    github_link.short_description = "GitHub"

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image', 'created_at')
    search_fields = ('title', 'description', 'tags')
    list_filter = ('created_at',)
    readonly_fields = ('preview_image',)
    
    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;"/>')
        return "Нет изображения"
    preview_image.short_description = "Превью"