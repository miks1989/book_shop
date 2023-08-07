from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'кніга'
        verbose_name_plural = 'кнігі'

    title = models.CharField(max_length=100, verbose_name='назва кнігі')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(User, related_name='books')
    likes = models.ManyToManyField(User, related_name='liked_books')
    count_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    likes = models.ManyToManyField(User, related_name='liked_comments')
