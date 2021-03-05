from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class NaoRecebidoManager(models.Manager):
    def get_queryset(self):
        return super(NaoRecebidoManager, self).get_queryset().filter(status='naoRecebido')

class Encomenda(models.Model):
    objects = models.Manager()
    naoRecebido = NaoRecebidoManager()
    STATUS = (('naoRecebido', 'Não Recebido'), ('recebido', 'Recebido'))
    TIPO_ENCOMENDA = (('envelope', 'Envelope'), ('caixa', 'Caixa'), ('pacote', 'Pacote'))
    RETIRADA = (('6', '6h'), ('12', '12h'), ('24', '24h'), ('48', '48h'), ('72', '72h'))
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='temCorrespondencia_encomendas')
    morador = models.CharField(max_length=60)
    tipo = models.CharField(choices=TIPO_ENCOMENDA, max_length=20)
    status = models.CharField(max_length=30, choices=STATUS)
    recebimento = models.DateTimeField(default=timezone.now)
    retirada = models.CharField(max_length=3, choices=RETIRADA, default='24')

    class Meta:
        ordering = ('-recebimento',)

    def __str__(self):
        return self.morador

    def get_absolute_url(self):
        return reverse('temCorrespondencia:detalhe_encomenda', args=[self.recebimento.year, self.recebimento.month, self.recebimento.day, self.morador])