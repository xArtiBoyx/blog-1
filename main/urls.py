from django.urls import path

from .views import home, second_view


urlpatterns = [
    path('', home, name='home'),
    path('second/', second_view, name='secondPage'),
]