from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from django.db.models import Count

from manager.models import Book, Comment


class Command(BaseCommand):

    def work(self, *args, **options):
        with transaction.atomic():
            book = Book.objects.create(title='test for tr')
            user1 = User.objects.first()
            book2 = Book.objects.create(title='test for tr')
            comment = Comment.objects.using('comments').create(text='text tr', book=book, user=user1)
            int('a')
            comment = Comment.objects.using('comments').create(text='text tr', book=book2, user=user1)