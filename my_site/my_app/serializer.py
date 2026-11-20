from rest_framework import serializers
from .models import Follow, Post, PostLike, Comment, CommentLike


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'following', 'created_date']


class FollowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'following']


class PostListSerializer(serializers.ModelSerializer):
    count_like = serializers.SerializerMethodField()
    count_comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_date', 'count_like', 'count_comment']

    def get_count_like(self, obj):
        return PostLike.objects.filter(post=obj, like=True).count()

    def get_count_comment(self, obj):
        return Comment.objects.filter(post=obj).count()


class PostDetailSerializer(serializers.ModelSerializer):
    count_like = serializers.SerializerMethodField()
    count_comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'description', 'created_date', 'count_like', 'count_comment']

    def get_count_like(self, obj):
        return PostLike.objects.filter(post=obj, like=True).count()

    def get_count_comment(self, obj):
        return Comment.objects.filter(post=obj).count()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'description']


# ---------- POST LIKE ----------

class PostLikeCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'like']


class PostLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user']


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'text']


class CommentDetailSerializer(serializers.ModelSerializer):
    count_like_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_date', 'count_like_comment']

    def get_count_like_comment(self, obj):
        return CommentLike.objects.filter(comment=obj, like=True).count()


class CommentLikeCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id', 'comment', 'like']


class CommentLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id', 'user']