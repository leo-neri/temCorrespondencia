from django.contrib import admin
from .models import Encomenda

# Register your models here.
@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'tipo', 'recebimento', 'retirada', 'status')
    list_filter = ('morador', 'tipo', 'status')
    search_fields = ('morador', 'tipo')
    # raw_id_fields = ('morador',)
    date_hierarchy = 'recebimento'
    ordering = ('status', 'recebimento')