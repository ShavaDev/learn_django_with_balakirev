"""
Данный файл, это файл, который представляет коллекцию маршрутов отдельного независимого приложения,
в данном случае hardware.
В итоге все маршруты, которые доступны в приложении hardware, у меня выделены отдельным файлом


Маршрутизатор (urls.py) смотрит ТОЛЬКО на путь.
Знак вопроса ? и всё, что идет после него, роутер Django просто отсекает. Он видит только /categories/music/,
успешно находит совпадение с шаблоном path('categories/<slug:cat_slug>/', ...) и передает в функцию параметр: cat_slug = "music"
GET-параметры НЕ попадают в аргументы функции автоматически.
Параметры name=Gagarina и key=pop Django помещает в специальный словарь внутри объекта запроса: request.GET


Почему в urls.py пишется '', а не '/'?В файле urls.py маршрутизатор Django заранее отрезает первый слеш у всех входящих
запросов для удобства обработки и объединения маршрутов через include().Браузер запрашивает:
/hardware/ Django внутри ищет: hardware/Браузер запрашивает: Django отрезает слэш, остается: ""
(пустая строка)Поэтому в urls.py корень описывается как path('', ...), а редирект для браузера всегда указывает конкретный путь: redirect('/').
"""

from django.urls import path, re_path, register_converter
from . import views
from . import converters


# специальная функция для регистрации конвертора
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.main_page, name="home"), # отвечает за главную страницу
    path('hardware/', views.hd, name="hardware"), # отвечает за страницу, где есть суффикс hardware/
    path('categories/<int:cat_id>/', views.categories, name="categories_id"), # отвечает за страницу, где есть суффикс categories/
    # в данном случае присутствует конвертор int (целое число), а после идет переменная, которое содержит число
    path('categories/<slug:cat_slug>/', views.categories_by_slug, name="categories_slug"), # другой инвертор slug, и символы и цифры
    # если по каким-то причинам конверторов недостаточно, тогда можно прописать свой:
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive), теперь вместо него можно написать:
    path("archive/<year4:year>/", views.archive, name="archive"),
    path("about/", views.about, name="about"),
]