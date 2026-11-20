import io
import os
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

from django.core.files.base import ContentFile
from PIL import Image

from my_app.models import Follow, Post, PostLike, Comment, CommentLike


def generate_image(text: str) -> ContentFile:
    color = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255),
    )
    img = Image.new("RGB", (400, 300), color=color)
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return ContentFile(buffer.read(), name=f"{text}.jpg")


def run():
    print("Очищаю старые данные...")
    CommentLike.objects.all().delete()
    Comment.objects.all().delete()
    PostLike.objects.all().delete()
    Post.objects.all().delete()
    Follow.objects.all().delete()

    print("Создаю Follow...")
    for i in range(20):
        Follow.objects.create(
            follower=random.randint(1, 50),
            following=random.randint(1, 50),
        )

    print("Создаю Post (с фото)...")
    posts = []
    for i in range(20):
        post = Post.objects.create(
            user=random.randint(1, 50),
            description=f"Тестовое описание поста №{i + 1}",
        )
        post.content.save(
            f"post_{i + 1}.jpg",
            generate_image(f"post_{i + 1}"),
            save=True,
        )
        posts.append(post)

    print("Создаю PostLike...")
    for i in range(20):
        PostLike.objects.create(
            user=random.randint(1, 50),
            post=random.choice(posts),
            like=random.choice([True, False]),
        )

    print("Создаю Comment...")
    comments = []
    for i in range(20):
        comment = Comment.objects.create(
            user=random.randint(1, 50),
            post=random.choice(posts),
            text=f"Тестовый комментарий №{i + 1}",
        )
        comments.append(comment)

    print("Создаю CommentLike...")
    for i in range(20):
        CommentLike.objects.create(
            user=random.randint(1, 50),
            comment=random.choice(comments),
            like=random.choice([True, False]),
        )

    print("Готово! Создано по 20 записей каждой модели.")


if __name__ == "__main__":
    run()