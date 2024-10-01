#Do django signals run in the same thread as the caller? 
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

s1="Yes, Django signals run in the same thread as the caller by default."
s2="This means that when a signal is sent, the receiver functions are executed in the same thread as  the code that sent the signal."
print(s1+s2)
#-----------------------------------------------------------------------------------------------------------------------#
import threading
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

# Simulate sending the signal
def send_signal():
    print(f"Signal sent from thread: {threading.current_thread().name}")
    request_finished.send(sender=None)

# Run the signal sending function
send_signal()

