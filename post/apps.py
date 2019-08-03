from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'
    list_display = ('title', 'slug', 'author')