from django import template
from django.http import HttpRequest, HttpResponse

import hardware.views as views

register = template.Library()

# простой тег для работы с данными
@register.simple_tag() # в скобках декоратора можно параметром name менять название тега
def get_categories() -> list:
    return views.categories_db

# включающий тег, позволяет создавать полноценные html страницы
@register.inclusion_tag('hardware/list_categories.html')
def show_categories(cat_selected=0) -> dict:
    cats = views.categories_db
    return {"cats": cats, "cat_selected": cat_selected}