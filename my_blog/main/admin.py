from django.contrib import admin
from .models import Post, Project, GalleryImage, MusicTrack
from django.utils.safestring import mark_safe
from django import forms
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import os

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


class MusicTrackForm(forms.ModelForm):
    class Meta:
        model = MusicTrack
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

@admin.register(MusicTrack)
class MusicTrackAdmin(admin.ModelAdmin):
    form = MusicTrackForm
    list_display = ('title', 'artist', 'duration', 'is_published', 'cover_preview', 'audio_player')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'artist', 'description')
    readonly_fields = ('cover_preview', 'audio_player_admin', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'artist')
        }),
        ('Медиа', {
            'fields': (
                'audio_file', 
                'audio_player_admin',
                'cover_image', 
                'cover_preview'
            )
        }),
        ('Метаданные', {
            'fields': ('created_at', 'is_published'),
        }),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return mark_safe(f'<img src="{obj.cover_image.url}" style="max-height: 200px;"/>')
        return "Нет обложки"
    cover_preview.short_description = "Превью обложки"

    def audio_player_admin(self, obj):
        if obj.audio_file:
            return mark_safe(f"""
                <audio controls style="width: 100%">
                    <source src="{obj.audio_file.url}" type="audio/mpeg">
                    Ваш браузер не поддерживает аудио элемент.
                </audio>
                <p><small>Файл: {obj.audio_file.name}</small></p>
            """)
        return "Аудио не загружено"
    audio_player_admin.short_description = "Аудиоплеер"

    def audio_player(self, obj):
        if obj.audio_file:
            return mark_safe(f"""
                <audio controls style="width: 100%; height: 30px;">
                    <source src="{obj.audio_file.url}" type="audio/mpeg">
                </audio>
            """)
        return "-"
    audio_player.short_description = "Плеер"

    def save_model(self, request, obj, form, change):
        if not obj.duration and obj.audio_file:
            # Здесь можно добавить логику определения длительности трека
            # Например, используя mutagen:
            # from mutagen.mp3 import MP3
            # audio = MP3(obj.audio_file)
            # obj.duration = int(audio.info.length)
            obj.duration = 0  # Временное значение
        super().save_model(request, obj, form, change)
