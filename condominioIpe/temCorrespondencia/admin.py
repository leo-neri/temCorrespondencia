from django.contrib import admin
from .models import Encomenda, Morador
from django.core.mail import send_mail

# Register your models here.
def enviaEmail(modeladmin, request, queryset):
    id_morador = list(queryset.values_list('morador_id', flat=True))[0]
    morador = Morador.objects.get(pk=id_morador)
    nome = morador.nome
    email = morador.email
    send_mail(
        'Nova encomenda para você!',
        f'Olá {nome}, uma nova encomenda chegou para você!',
        'mestresdopython@gmail.com',
        [email],
        fail_silently=False,
    )

enviaEmail.short_description = "Enviar email para os selecionados"

class EncomendaAdmin(admin.ModelAdmin):

    # readonly_fields = ['autor']
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     Encomenda.autor = request.user
    #     return super().get_form(request, obj, **kwargs)

    list_display = ('morador', 'tipo', 'recebimento', 'status', 'autor')
    list_filter = ('morador', 'tipo', 'status')
    search_fields = ('morador', 'tipo')
    raw_id_fields = ('autor',)
    date_hierarchy = 'recebimento'
    ordering = ('status', 'recebimento')

    actions = [enviaEmail]

admin.site.register(Encomenda, EncomendaAdmin)


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'torre', 'apartamento', 'email', 'telefone')
