from django.urls import path
from backend.servico import views as V

app_name = 'servico'
urlpatterns = [
    path('', V.ordem_servico_list, name='ordem_servico_list'),
    path('create/', V.ordem_servico_create, name='ordem_servico_create'),
    path('<int:pk>/', V.ordem_servico_detail, name='ordem_servico_detail'),
    # path('<int:pk>/update', V.servico_ordem_update, name='servico_ordem_update'),
    # path('<int:pk>/delete', V.servico_ordem_delete, name='servico_ordem_delete'),
]