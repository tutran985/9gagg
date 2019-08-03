from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.exceptions import ParseError

class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    users_like = serializers.PrimaryKeyRelatedField(queryset= User.objects.all(), many=True)
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'users_like', 'created_at','updated_at')

    def validate(self, attrs):
        if not attrs.get('description') and not attrs.get('image'):
            raise ParseError({
                "error_code" : 4000,
                "message" : "Khong duoc de trong ca 2 truong image va description"

            })
        return attrs

class UserSerializers(serializers.ModelSerializer):
    # post = serializers.PrimaryKeyRelatedField(many= True, queryset=Post.objects.all())
    author =  PostSerializers(many=True, read_only=True)
    posts_liked = PostSerializers(many=True, read_only=True)
    class Meta:
        model = User
        fields =  ('id', 'username', 'author','posts_liked')