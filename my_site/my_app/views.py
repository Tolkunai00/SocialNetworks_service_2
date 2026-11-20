from rest_framework import generics, permissions

from .models import Follow, Post, PostLike, Comment, CommentLike
from .serializer import (
    FollowListSerializer, FollowCreateSerializer,
    PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer,
    PostLikeCreateDeleteSerializer, PostLikeListSerializer,
    CommentCreateUpdateSerializer, CommentDetailSerializer,
    CommentLikeCreateDeleteSerializer, CommentLikeListSerializer,
)


# ---------- FOLLOW ----------

class FollowListView(generics.ListAPIView):
    serializer_class = FollowListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user.id)


class FollowCreateView(generics.CreateAPIView):
    serializer_class = FollowCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user.id)


class FollowDeleteView(generics.DestroyAPIView):
    serializer_class = FollowListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user.id)


# ---------- POST ----------

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user.id)


class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user.id)


# ---------- POST LIKE ----------

class PostLikeCreateView(generics.CreateAPIView):
    serializer_class = PostLikeCreateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)


class PostLikeDeleteView(generics.DestroyAPIView):
    serializer_class = PostLikeCreateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PostLike.objects.filter(user=self.request.user.id)


class PostLikeListView(generics.ListAPIView):
    """Список лайкнувших конкретный пост: /posts/<post_id>/likes/"""
    serializer_class = PostLikeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return PostLike.objects.filter(post_id=post_id, like=True)


# ---------- COMMENT ----------

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)


class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user.id)


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user.id)


class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- COMMENT LIKE ----------

class CommentLikeCreateView(generics.CreateAPIView):
    serializer_class = CommentLikeCreateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)


class CommentLikeDeleteView(generics.DestroyAPIView):
    serializer_class = CommentLikeCreateDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CommentLike.objects.filter(user=self.request.user.id)


class CommentLikeListView(generics.ListAPIView):
    """Список лайкнувших конкретный комментарий: /comments/<comment_id>/likes/"""
    serializer_class = CommentLikeListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        comment_id = self.kwargs.get('comment_id')
        return CommentLike.objects.filter(comment_id=comment_id, like=True)