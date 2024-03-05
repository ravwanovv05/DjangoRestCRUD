from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models.posts import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'description')


