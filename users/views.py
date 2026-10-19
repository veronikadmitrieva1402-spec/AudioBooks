from django.http import HttpResponse
from homepage.views import page


def user_list(request):
    content = """
    <h1>Пользователи</h1>
    <p>Список пользователей сервиса.</p>
    """
    return HttpResponse(page("Пользователи", content))