from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.CharField(max_length=200)
    size = models.CharField(max_length=50)

    def prepare(self):
        from .signals import pizza_done
        print(f"Preparing pizza {self.name}...")
        
        # Fire custom signal
        pizza_done.send(sender=self.__class__, toppings=self.toppings, size=self.size)

    def __str__(self):
        return self.name
