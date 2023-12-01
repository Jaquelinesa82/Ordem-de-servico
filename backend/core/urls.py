from django.urls import path
from backend.core import views as V

app_name = 'core'
urlpatterns = [
    path('', V.index, name='index'),
]