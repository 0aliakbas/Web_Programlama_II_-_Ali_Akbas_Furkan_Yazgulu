import django.dispatch
from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

# 1. Custom Signal
pizza_done = django.dispatch.Signal()

@receiver(pizza_done)
def notify_pizza_ready(sender, **kwargs):
    toppings = kwargs.get('toppings')
    size = kwargs.get('size')
    print(f"\n[CUSTOM SIGNAL RECEIVED from {sender.__name__}]")
    print(f"--> Pizza is ready! Size: {size}, Toppings: {toppings}\n")

# 2. Built-in Signal (post_save on User)
@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print(f"\n[BUILT-IN SIGNAL RECEIVED (post_save)]: Profile created for NEW user: {instance.username}\n")
    else:
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()
            print(f"\n[BUILT-IN SIGNAL RECEIVED (post_save)]: Profile updated for EXISTING user: {instance.username}\n")

# 3. Built-in Signal (request_finished)
@receiver(request_finished)
def my_request_callback(sender, **kwargs):
    print("\n[BUILT-IN SIGNAL RECEIVED (request_finished)]: An HTTP request has finished!\n")
