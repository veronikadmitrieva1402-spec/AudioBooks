from django.http import HttpResponse
from homepage.views import page
from storage import load_audiobooks
from models import Audiobook


def book_list(request):
    books = load_audiobooks("data/audiobooks.json")
    items = ""
    if not books:
        items = '<li class="list-group-item">Коллекция пуста.</li>'
    else:
        for book in books:
            duration = Audiobook.format_duration(book.total_minutes)
            items += f"""
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <strong>{book.title}</strong> — {book.author} 
                    <br><small class="text-muted">Чтец: {book.narrator} | {duration}</small>
                </div>
                <a href="/books/{book.id}/" class="btn btn-sm btn-outline-primary">Подробнее</a>
            </li>
            """
    content = f"""
    <h1 class="mb-4">Коллекция аудиокниг</h1>
    <ul class="list-group shadow-sm">
        {items}
    </ul>
    """
    return HttpResponse(page("Книги", content))


def book_detail(request, book_id):
    books = load_audiobooks("data/audiobooks.json")
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        content = """
        <div class="alert alert-danger">
            <h1>Аудиокнига не найдена</h1>
        </div>
        <a href="/books/" class="btn btn-outline-secondary">← К списку</a>
        """
        return HttpResponse(page("Не найдено", content), status=404)

    duration = Audiobook.format_duration(book.total_minutes)
    real_duration = Audiobook.format_duration(book.real_minutes)
    content = f"""
    <div class="card shadow-sm">
        <div class="card-body">
            <h2 class="card-title">{book.title}</h2>
            <h6 class="card-subtitle mb-2 text-muted">{book.author}</h6>
            <p class="card-text mt-3">
                <strong>Жанр:</strong> {book.genre}<br>
                <strong>Чтец:</strong> {book.narrator}<br>
                <strong>Длительность:</strong> {duration}<br>
                <strong>При скорости x{book.speed}:</strong> {real_duration}<br>
                <strong>Статус:</strong> {'✅ Прослушано' if book.is_finished else '📖 В процессе'}
            </p>
            <a href="/books/" class="btn btn-outline-secondary mt-3">← Назад к списку</a>
        </div>
    </div>
    """
    return HttpResponse(page(book.title, content))