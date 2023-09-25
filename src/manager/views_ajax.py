from django.http import HttpResponse, JsonResponse

from manager.models import Book


def add_like_ajax(request):
    if request.user.is_authenticated:
        print(request.GET.get('book_id'))
        book_id = request.GET.get('book_id')
        book = Book.objects.get(id=book_id)
        if request.user in book.likes.all():
            book.likes.remove(request.user)
            book.count_likes -= 1
        else:
            book.likes.add(request.user)
            book.count_likes += 1
        book.save()
        count_likes = book.count_likes

        return JsonResponse({'count_likes': count_likes}, status=201)
    return JsonResponse({'error': 'i do not know you'}, status=403)
