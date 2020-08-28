from rest_framework import serializers
from .models import Post, Reply


class PostSerializer(serializers.ModelSerializer):
    author_str = serializers.SerializerMethodField()
    liked_user_count = serializers.SerializerMethodField()

    def get_author_str(self, obj) -> str:
        return obj.author.author_str

    def get_liked_user_count(self, obj) -> int:
        return obj.liked_users.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author_str',
            'liked_user_count',
        )


class ReplySerializer(serializers.ModelSerializer):
    author_str = serializers.SerializerMethodField()
    liked_user_count = serializers.SerializerMethodField()

    def get_author_str(self, obj) -> str:
        return obj.author.author_str

    def get_liked_user_count(self, obj) -> int:
        return obj.liked_users.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'reply_order',
            'content',
            'author_str',
            'liked_user_count',
        )

