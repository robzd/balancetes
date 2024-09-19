from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('criarbalancete/', views.criarbalancete, name='criarbalancete'),
    path('listarbalancetes/', views.listarbalancetes, name='listarbalancetes'),
    path('<int:balancete_id>/verbalancete/', views.verbalancete, name='verbalancete'),
    path('<int:balancete_id>/addreceitadespesa/', views.addreceitadespesa, name='addreceitadespesa'),
]