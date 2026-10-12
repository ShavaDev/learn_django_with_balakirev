"""
URL configuration for sitetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hardware import views
from hardware.views import page_not_found, server_error

# такой пример конечно не плохой, но для другого проекта надо будет все эти маршруты копировать, что не удобно
# следовательно, можно воспользоваться функцией include(), и вынести все маршруты в отдельный файл hardware/urls.py
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.main_page), # http://127.0.0.1:8000/
#     path('hardware/', views.index), # первый параметр, суффикс, это часть url который добавляется после доменного имени, а второй аргумент это функция ссылка на функцию представления
#     path('categories/', views.categories),
# ]
# и написать вот таким образом все
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hardware/', include('hardware.urls')), # теперь будет главный url адрес иметь маршрут http://127.0.0.1:8000/hardware/
    path('', include('hardware.urls')),
]

# специальныe обработчики
handler404 = page_not_found
handler500 = server_error