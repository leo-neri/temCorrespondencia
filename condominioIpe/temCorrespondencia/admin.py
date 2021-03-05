from django.contrib import admin
from .models import Encomenda

# Register your models here.
@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'tipo', 'recebimento', 'status', 'autor')
    list_filter = ('morador', 'tipo', 'status')
    search_fields = ('morador', 'tipo')
    raw_id_fields = ('autor',)
    date_hierarchy = 'recebimento'
    ordering = ('status', 'recebimento')