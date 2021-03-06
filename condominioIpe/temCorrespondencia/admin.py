from django.contrib import admin
from .models import Encomenda, Morador

# Register your models here.
@admin.register(Encomenda)
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


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'torre', 'apartamento', 'email', 'telefone')
