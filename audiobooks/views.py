from django.shortcuts import render
from storage import load_audiobooks


def book_list(request):
    books = load_audiobooks("data/audiobooks.json")
    context = {
        "books": books,
    }
    return render(request, "audiobooks/book_list.html", context)


def book_detail(request, book_id):
    books = load_audiobooks("data/audiobooks.json")
    book = next((b for b in books if b.id == book_id), None)
    context = {
        "book": book,
    }
    return render(
        request,
        "audiobooks/book_detail.html",
        context,
        status=404 if book is None else 200
    )
