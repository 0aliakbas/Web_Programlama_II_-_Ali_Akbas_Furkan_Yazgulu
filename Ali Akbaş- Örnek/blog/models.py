from django.db import models
from django.utils import timezone

class Makale(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Başlık")
    icerik = models.TextField(verbose_name="İçerik")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"


class SistemLog(models.Model):
    islem_tipi = models.CharField(max_length=100, verbose_name="İşlem Tipi")
    mesaj = models.TextField(verbose_name="Mesaj/Açıklama")
    tarih = models.DateTimeField(default=timezone.now, verbose_name="Tarih")

    def __str__(self):
        return f"{self.islem_tipi} - {self.tarih.strftime('%d.%m.%Y %H:%M')}"

    class Meta:
        verbose_name = "Sistem Logu"
        verbose_name_plural = "Sistem Logları"
