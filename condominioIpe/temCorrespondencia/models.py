from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cpf_field.models import CPFField
from django.urls import reverse


# Create your models here.
class Morador(models.Model):
    TORRES = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'))
    nome = models.CharField(max_length=50)
    torre = models.CharField(max_length=1, choices=TORRES)
    apartamento = models.CharField(max_length=2, default='')
    cpf = CPFField('CPF')
    email = models.EmailField()
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name_plural = "Moradores"

    def __str__(self):
        return self.nome

class NaoRecebidoManager(models.Manager):
    def get_queryset(self):
        return super(NaoRecebidoManager, self).get_queryset().filter(status='naoRecebido')

class Encomenda(models.Model):
    objects = models.Manager()
    naoRecebido = NaoRecebidoManager()
    STATUS = (('naoRecebido', 'Não Retirado'), ('recebido', 'Retirado'))
    TIPO_ENCOMENDA = (('envelope', 'Envelope'), ('caixa', 'Caixa'), ('pacote', 'Pacote'))
    RETIRADA = (('6', '6h'), ('12', '12h'), ('24', '24h'), ('48', '48h'), ('72', '72h'))
    autor = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='temCorrespondencia_moradores')
    torre = models.CharField(max_length=1, editable=False, null=True, blank=True, default='')
    tipo = models.CharField(choices=TIPO_ENCOMENDA, max_length=20)
    status = models.CharField(max_length=30, choices=STATUS)
    recebimento = models.DateTimeField(default=timezone.now)
    retirada = models.CharField(max_length=3, choices=RETIRADA, default='24')

    class Meta:
        ordering = ('-recebimento',)

    def __str__(self):
        return self.morador.nome

    def get_absolute_url(self):
        return reverse('temCorrespondencia:detalhe_encomenda', args=[self.recebimento.year, self.recebimento.month, self.recebimento.day, self.morador.nome])

