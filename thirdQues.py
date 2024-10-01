#By default do django signals run in the same database transaction as the caller? 
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.
s1="By default, Django signals do not run in the same database transaction as the caller. "
s2="Instead, they run in autocommit mode, meaning each database query is executed and committed immediately"
print(s1+s1)  #Answer
#--------------------------------------------------------------------------------------------------------------#
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_callback(sender, instance, **kwargs):
    print("Signal received. Checking transaction status...")
    print(f"Inside signal, transaction status: {transaction.get_autocommit()}")

def create_user():
    print("Creating user. Checking transaction status...")
    print(f"Before user creation, transaction status: {transaction.get_autocommit()}")
    user = User.objects.create(username='testuser')
    print(f"After user creation, transaction status: {transaction.get_autocommit()}")

# Run the function to create a user
create_user()
