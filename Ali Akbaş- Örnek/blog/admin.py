from django.contrib import admin
from .models import Makale, SistemLog

@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'olusturulma_tarihi')
    search_fields = ('baslik',)

@admin.register(SistemLog)
class SistemLogAdmin(admin.ModelAdmin):
    list_display = ('islem_tipi', 'tarih', 'mesaj')
    list_filter = ('islem_tipi', 'tarih')
    readonly_fields = ('islem_tipi', 'mesaj', 'tarih') # Loglar manuel olarak değiştirilemesin
