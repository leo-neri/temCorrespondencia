from django.shortcuts import render, get_object_or_404
from .models import Encomenda


# Create your views here.
def lista_encomendas(request):
    encomendas = Encomenda.naoRecebido.all()
    return render(request, 'temCorrespondencia/encomenda/lista.html', {'encomendas': encomendas})

def detalhe_encomenda(request, ano, mes, dia, morador):
    encomenda = get_object_or_404(Encomenda, status='naoRecebido', morador=morador, recebimento__year=ano, recebimento__month   =mes, recebimento__day=dia,)
    return render(request, 'temCorrespondencia/encomenda/detalhe.html', {'encomenda': encomenda})
