from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string


def hd(request: HttpRequest) -> HttpResponse: # hardware
    """
    request - это ссылка на специальный класс HttpRequest, и содержит информацию о запросе (сессия, куках и так далее)
    то есть через этот параметр нам будет доступна вся информация о запросе
    :param request:
    :return:
    """
    return HttpResponse("Страница приложения hardware")

def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Страница с категориями</h1><p>id: {cat_id}</p>")


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    # метод .get('ключ') вернет None или значение по умолчанию, если параметра нет
    name = request.GET.get("name", "не указано")
    key = request.GET.get("key", "не указано")
    print(request.GET)
    return HttpResponse(
        f"<h1>Статьи по категориям</h1>"
        f"<p>slug: {cat_slug}</p>"
        f"<p>Имя: {name}</p>"
        f"<p>Ключ: {key}</p>"
    )


def archive(request: HttpRequest, year: int) -> HttpResponse:
    if year > 2026:
        # raise Http404()
        # return redirect("/") # для перенаправления с кодом 302 (временный url адрес)
        # return redirect("/", permanent=True) # для перенаправления с кодом 301 (постоянный url адрес)
        # вместо 1-го аргумента можно прописывать не только адрес url, но и функцию представления
        # return redirect(index)
        # return redirect("home") # можно прописывать и имя маршрута
        # return redirect("categories_slug", cat_slug=year) # второй аргумент это значение слага, можно в кавычках любое слово написать, в маршруте так и будет указано
        uri = reverse('categories_slug', args=("music",)) # это то же самое что и прошлая строка
        return redirect(uri) # просто разделил 'обязанности', обязательно в args идет кортеж
    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}</p>")


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
class Myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def main_page(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("<h1><ul>Главная страница</ul></h1>")
    # t = render_to_string("hardware/index.html")
    # return HttpResponse(t)
    # предыдущие две строчки можно объединить одной строкой
    data = {"title": 'Главная страница',
            "menu": menu,
            "float": 28.65,
            "lst": [1, 2, True, {1,2}, 'abs'],
            "set": {1,2,3},
            "dict": {"k1": "val1", "k2": "val2"},
            "class": Myclass(10, 20)}
    return render(request, "hardware/index.html", context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "hardware/about.html", context={"title": "О сайте"})


def page_not_found(request: HttpRequest, exception: Exception | Http404) -> HttpResponse:
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")
