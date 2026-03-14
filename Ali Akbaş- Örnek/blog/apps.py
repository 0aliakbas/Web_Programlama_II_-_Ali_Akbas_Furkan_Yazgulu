from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Blog ve Log Yönetimi'

    def ready(self):
        # Bu kısım çok önemli! Sinyallerin çalışması için projeye dahil edilmesi gerekir.
        # Bu yüzden ready() metodu içinde signals dosyasını import ediyoruz.
        import blog.signals
