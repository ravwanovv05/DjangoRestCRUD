from modeltranslation.translator import TranslationOptions, register
from main.models.posts import Post


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'description')
