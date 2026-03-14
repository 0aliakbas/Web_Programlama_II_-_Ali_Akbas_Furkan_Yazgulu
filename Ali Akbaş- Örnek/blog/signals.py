from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Makale, SistemLog

# 1. 'post_save' sinyalini dinleyerek yeni makale EKLENDİĞİNDE çalışacak fonksiyon
@receiver(post_save, sender=Makale)
def makale_eklendi_logla(sender, instance, created, **kwargs):
    if created:
        SistemLog.objects.create(
            islem_tipi="YENİ MAKALE (EKLEME)",
            mesaj=f"Sisteme yeni bir makale eklendi. Başlık: '{instance.baslik}'"
        )
        print(f"SİNYAL ÇALIŞTI: '{instance.baslik}' eklendi logu oluşturuldu.")
    else:
        # created False ise veri güncellenmiş demektir
        SistemLog.objects.create(
            islem_tipi="MAKALE GÜNCELLEME",
            mesaj=f"Mevcut makale güncellendi. Başlık: '{instance.baslik}'"
        )
        print(f"SİNYAL ÇALIŞTI: '{instance.baslik}' güncellendi logu oluşturuldu.")


# 2. 'post_delete' sinyalini dinleyerek bir makale SİLİNDİĞİNDE çalışacak fonksiyon
@receiver(post_delete, sender=Makale)
def makale_silindi_logla(sender, instance, **kwargs):
    SistemLog.objects.create(
        islem_tipi="MAKALE SİLİNME",
        mesaj=f"Bir makale sistemden silindi. Silinen Başlık: '{instance.baslik}'"
    )
    print(f"SİNYAL ÇALIŞTI: '{instance.baslik}' silindi logu oluşturuldu.")
