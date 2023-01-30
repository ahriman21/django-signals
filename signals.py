#  this is scenario : we have two models 'User' and 'Profile' when an instance of User created, we want to create an profile instance automatically.
#  the  '@reciver' decorator links the sender model to our funtion
#  'sender' is the object that provokes our function to do something.
#  

#signals.py:
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        
 
