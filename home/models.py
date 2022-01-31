from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import (get_current_user, 
                                           get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField

class StocksTickers(models.Model):
    ticker = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    
    
    def __str__(self):
        return str(self.ticker)
    
    
    
    
