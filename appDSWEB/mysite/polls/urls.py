from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('criarbalancete/', views.criarbalancete, name='criarbalancete'),
    path('listarbalancetes/', views.listarbalancetes, name='listarbalancetes'),
    path('<int:balancete_id>/verbalancete/', views.verbalancete, name='verbalancete'),
    path('<int:balancete_id>/addreceitadespesa/', views.addreceitadespesa, name='addreceitadespesa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)