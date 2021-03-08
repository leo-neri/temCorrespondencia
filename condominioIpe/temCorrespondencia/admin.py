from django.contrib import admin
from .models import Encomenda, Morador
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy
from datetime import datetime, timezone, timedelta

# Register your models here.

def enviaEmail(modeladmin, request, queryset):
    prazo = str(list(queryset.values_list('retirada', flat=True))[0])
    recebimento = list(queryset.values_list('recebimento', flat=True))[0]
    # print(recebimento)
    agora = datetime.now(tz=timezone(timedelta(0)))
    diferenca_segundos = (agora-recebimento).total_seconds()
    prazo_segundos = int(prazo)*3600
    if diferenca_segundos >= prazo_segundos:
        id_morador = list(queryset.values_list('morador_id', flat=True))[0]
        morador = Morador.objects.get(pk=id_morador)
        nome = morador.nome
        email = morador.email
        tipo = str(list(queryset.values_list('tipo', flat=True))[0]).capitalize()
        corpo = f'Olá {nome}, não esqueça de retirar sua nova encomenda de tipo {tipo}! O seu antigo prazo de retirada de {prazo}h já expirou! Venha retirá-la!'
        send_mail(
            'Retire sua encomenda!',
            corpo,
            'encomendasipe@gmail.com',
            [email],
            fail_silently=False,
        )

enviaEmail.short_description = "Enviar email para os selecionados"

class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'tipo', 'recebimento', 'status', 'autor', 'torre')
    list_filter = ('morador', 'tipo', 'status', 'torre')
    search_fields = ('morador', 'tipo')
    raw_id_fields = ('autor',)
    date_hierarchy = 'recebimento'
    ordering = ('status', '-recebimento')
    actions = [enviaEmail]

    def save_model(self, request, obj, form, change):
        obj.torre = str(Morador.objects.get(nome=obj).torre).upper()
        if not obj.autor:
            obj.autor = request.user
        obj.save()

admin.site.register(Encomenda, EncomendaAdmin)


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'torre', 'apartamento', 'email', 'telefone')

from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=Encomenda)
def my_handler(sender, instance, created, **kwargs):
    if created:
        tipo = instance.tipo.capitalize()
        prazo = instance.retirada
        morador = Morador.objects.get(nome=str(instance))
        nome = morador.nome
        email = morador.email
        corpo = f'Olá {nome}, uma nova encomenda de tipo {tipo} chegou para você! O seu prazo de retirada é de {prazo}h. Venha retirá-la!'
        send_mail(
            'Nova encomenda para você!',
            corpo,
            'encomendasipe@gmail.com',
            [email],
            fail_silently=False,
        )