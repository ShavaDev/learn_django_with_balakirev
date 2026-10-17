from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify # от туда можно импортировать функции фильтров шаблонов


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


menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]
# class Myclass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b


data_db = [
    {"id": 1, "title": "Графический процессор", "content": """<h1>Графический процессор</h1> (англ. graphics processing unit, GPU) — отдельное устройство 
персонального компьютера или игровой приставки, выполняющее графический рендеринг; в начале 2010-х годов графические 
процессоры стали массово применяться и в других устройствах: планшетные компьютеры, встраиваемые системы, цифровые телевизоры.
Современные графические процессоры очень эффективно обрабатывают и отображают компьютерную графику, благодаря 
специализированной конвейерной архитектуре они намного эффективнее в обработке графической информации, чем типичный центральный процессор.
Графический процессор в современных видеоадаптерах применяется в качестве ускорителя трёхмерной графики.
Может применяться как в составе дискретной видеокарты, так и в интегрированных решениях (встроенных в северный мост либо в гибридный процессор).""", "is_published": True},
    {"id": 2, "title": "Центральный процессор", "content": "Описание центрального процессора", "is_published": False},
    {"id": 3, "title": "Материнская плата", "content": "Описание материнской платы", "is_published": True}
]


categories_db = [
    {"id": 1, "name": "Процессоры (CPU)"},
    {"id": 2, "name": "Видеокарты (GPU)"},
    {"id": 3, "name": "Материнские платы"},
    {"id": 4, "name": "Оперативная память"},
    {"id": 5, "name": "Хранение данных (SSD/HDD)"},
]


def main_page(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("<h1><ul>Главная страница</ul></h1>")
    # t = render_to_string("hardware/index.html")
    # return HttpResponse(t)
    # предыдущие две строчки можно объединить одной строкой
    # data = {"title": 'главная страница',
    #         "menu": menu,
    #         "float": 28.65,
    #         "lst": [1, 2, True, {1,2}, 'abs'],
    #         "set": {1,2,3},
    #         "dict": {"k1": "val1", "k2": "val2"},
    #         "class": Myclass(10, 20),
    #         "url": slugify("The Main Page")}
    data = {
        "title": "Главная страница",
        "menu": menu,
        "posts": data_db,
        "cat_selected": 0,
    }
    return render(request, "hardware/index.html", context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "hardware/about.html", context={"title": "О сайте", "menu": menu})


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f"Отображение поста с id = {post_id}")


def addpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Обратная связь")


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data = {
        "title": "Главная страница",
        "menu": menu,
        "posts": data_db,
        "cat_selected": 0,
    }
    return render(request, "hardware/index.html", context=data)


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


def page_not_found(request: HttpRequest, exception: Exception | Http404) -> HttpResponse:
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")


def server_error(request: HttpRequest) -> HttpResponse:
    return HttpResponseNotFound("<h1>Ошибка со стороны сервера</h1>")
