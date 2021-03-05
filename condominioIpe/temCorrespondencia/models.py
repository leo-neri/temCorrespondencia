from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Encomenda(models.Model):
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
