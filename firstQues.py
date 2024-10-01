# Question 1: By default are django signals executed synchronously or asynchronously? 
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic

s1="Answer: By default, Django signals are executed synchronously. This means that when a signal is triggered," 
s2=" all connected receiver functions are called one after another, and each must complete before the next one starts"
print(s1+s2)

#---------------------------------------------------------------------------------------------------------------------#
import time
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Signal received. Starting task...")
    time.sleep(5)  # Simulate a long-running task
    print("Task completed.")

# Simulate sending the signal
print("Sending signal...")
request_finished.send(sender=None)
print("Signal sent.")

