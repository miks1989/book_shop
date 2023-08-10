from django.core.management import BaseCommand
from django.db.models import Count

from manager.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.annotate(likes_book=Count('likes'))
        for book in books:
            book.count_likes = book.likes_book
            print(book.count_likes)

        Book.objects.bulk_update(books, ['count_likes'], batch_size=1000)
