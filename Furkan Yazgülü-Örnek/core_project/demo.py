import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from django.contrib.auth.models import User
from signals_demo.models import Pizza
from django.core.signals import request_finished

def run():
    print("======================================================")
    print("   TESTING DJANGO SIGNALS (BUILT-IN AND CUSTOM)")
    print("======================================================\n")
    
    # Clean up before testing
    User.objects.all().delete()
    Pizza.objects.all().delete()

    print("1. Testing Built-in Signal (post_save on User)")
    print("------------------------------------------------------")
    print("> Action: Creating a new user 'alice'...")
    user = User.objects.create_user('alice', 'alice@example.com', 'password123')
    print("> Result: User created.")

    print("\n> Action: Updating the user's email...")
    user.email = 'alice_updated@example.com'
    user.save()
    print("> Result: User updated.\n")
    
    print("======================================================")
    print("2. Testing Custom Signal (pizza_done on Pizza)")
    print("------------------------------------------------------")
    print("> Action: Creating a new pizza and preparing it...")
    pizza = Pizza.objects.create(name='Margarita', size='Large', toppings='Cheese, Tomato')
    pizza.prepare()
    print("\n======================================================")
    print("3. Testing Built-in Signal (request_finished)")
    print("------------------------------------------------------")
    print("> Action: Manually firing request_finished signal...")
    request_finished.send(sender=None)
    print("======================================================\n")

if __name__ == '__main__':
    run()
