from django.urls import path
from . import views

urlpatterns = [
    path('', views.TarefaLista.as_view(), name='lista'),
    path('nova/', views.TarefaCriar.as_view(), name='criar'),
    path('<int:pk>/editar/', views.TarefaEditar.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.TarefaExcluir.as_view(), name='excluir'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
]