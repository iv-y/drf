from rest_framework import serializers
from board.models import Post, Reply


class PostSerializer(serializers.ModelSerializer):
    liked_user_count = serializers.SerializerMethodField()

    def get_liked_user_count(self, obj) -> int:
        return obj.liked_users.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author',
            'anonymous',
            'author_str',
            'liked_user_count',
        )
        read_only_fields = (
            'id',
            'author_str',
            'liked_user_count',
        )
        extra_kwargs = {
            'author': {'write_only': True},
            'anonymous': {'write_only': True},
        }


class ReplySerializer(serializers.ModelSerializer):
    liked_user_count = serializers.SerializerMethodField()

    def get_liked_user_count(self, obj) -> int:
        return obj.liked_users.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'reply_order',
            'content',
            'author',
            'anonymous',
            'author_str',
            'liked_user_count',
        )
        read_only_fields = (
            'id',
            'author_str',
            'liked_user_count',
        )
        extra_kwargs = {
            'author': {'write_only': True},
            'anonymous': {'write_only': True},
        }

