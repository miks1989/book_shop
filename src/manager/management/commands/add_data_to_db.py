from django.contrib.auth.models import User
from django.core.management import BaseCommand

from manager.models import Book


class Command(BaseCommand):
    help = "add simple data to db"

    def handle(self, *args, **options):
        Book.objects.all().delete()
        # User.objects.create(username='Boris', password='useruser')
        # User.objects.create(username='Tony', password='useruser')
        # user1 = User(username='Boris', password='useruser')
        # user2 = User(username='Tony', password='useruser')
        # user3 = User(username='Petya', password='useruser')
        # User.objects.bulk_create([user2, user3])
        users = User.objects.all()
        book1 = Book(title='book1', text='text for book 1')
        book2 = Book(title='book2', text='text for book 2')
        book3 = Book(title='book3', text='text for book 3')
        Book.objects.bulk_create([book1, book2, book3])

        for book in Book.objects.all():
            book.authors.add(users[0], users[2])
            book.save()




