from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE,blank=True,null=True)
    state = models.CharField(max_length=100)
    zip = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=14)
    image = models.ImageField(upload_to='profile/') 
    def __str__(self):
        return str(self.user)
    

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) 
class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Models for stocks followed by user


class UserFollowedStocks(models.Model):
    user_followed_stocks = models.CharField(max_length=30,unique=True)
    def save(self, *args, **kwargs):
      if UserFollowedStocks.objects.count() > 3:
        return
      super(UserFollowedStocks, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.user_followed_stocks)
