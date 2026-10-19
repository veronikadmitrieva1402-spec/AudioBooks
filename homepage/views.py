from django.http import HttpResponse


def page(title, content):
    """Единый каркас HTML-страницы."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">🎧 Аудиокниги</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/books/">Книги</a>
                <a class="nav-link" href="/users/">Пользователи</a>
            </div>
        </div>
    </nav>
    <main class="container">
        {content}
    </main>
</body>
</html>"""


def index(request):
    content = """
    <div class="p-5 mb-4 bg-white rounded-3 shadow-sm">
        <h1 class="display-5 fw-bold">Сервис учёта аудиокниг</h1>
        <p class="lead">Веб-версия вашего проекта.</p>
        <a href="/books/" class="btn btn-primary btn-lg">Перейти к книгам</a>
    </div>
    """
    return HttpResponse(page("Главная", content))


def page_not_found(request, exception):
    content = """
    <div class="text-center mt-5">
        <h1 class="display-1 text-danger">404</h1>
        <p class="lead">Страница не найдена.</p>
        <a href="/" class="btn btn-primary">На главную</a>
    </div>
    """
    return HttpResponse(page("404 - Не найдено", content), status=404)