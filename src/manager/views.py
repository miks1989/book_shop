from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from manager.models import Book, Comment


class BookView(View):

    def get(self, request):
        comments_for_prefetch = Prefetch('comments',
                                         queryset=Comment.objects.select_related('user').
                                         annotate(likes_comment=Count('likes')))
        data = {'books': Book.objects.
        prefetch_related(comments_for_prefetch, 'authors').
        annotate(likes_book=Count('likes'))}
        # data = {'books': Book.objects.all()}
        return render(request, 'index.html', context=data)


class AddLikeView(View):
    def get(self, request, book_id):
        if request.user.is_authenticated:
            book = Book.objects.get(id=book_id)
            if request.user in book.likes.all():
                book.likes.remove(request.user)
            else:
                book.likes.add(request.user)
        return redirect('list_view')
