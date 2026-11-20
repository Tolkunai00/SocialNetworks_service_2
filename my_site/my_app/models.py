from django.db import models


class Follow(models.Model):
    follower = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.follower} → {self.following}"


class Post(models.Model):
    user = models.PositiveIntegerField()
    content = models.FileField(upload_to='content/', null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Post {self.id} by user {self.user}"


class PostLike(models.Model):
    user = models.PositiveIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user} liked post {self.post_id}"


class Comment(models.Model):
    user = models.PositiveIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Comment by user {self.user} on post {self.post_id}"


class CommentLike(models.Model):
    user = models.PositiveIntegerField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user} liked comment {self.comment_id}"