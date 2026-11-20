from django.contrib import admin
from .models import Follow, Post, PostLike, Comment

admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)