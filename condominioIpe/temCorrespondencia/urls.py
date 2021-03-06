from django.urls import path
from . import views

app_name = 'temCorrespondencia'

urlpatterns = [
    path('', views.lista_encomendas, name='lista_encomendas'),
    path('<int:ano>/<int:mes>/<int:dia>/<slug:morador>', views.detalhe_encomenda, name='detalhe_encomenda')
]
