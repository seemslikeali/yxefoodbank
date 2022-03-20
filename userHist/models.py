from django.db import models
from account.models import Account

# Create your models here.





class Orders(models.Model):
    user_name = models.CharField(max_length=200, null = True, blank = True)
    order_ID = models.IntegerField(default=0, null=True, blank=True)
    order_Date = models.DateTimeField(auto_now_add=False, auto_now=False, null = True)

    def __str__(self):
        return str(self.id)

class OrderHistory(models.Model):
    user_name = models.CharField(max_length=200, null = True, blank = True)
    order_ID = models.IntegerField(default=0, null=True, blank=True)
    order_Date = models.DateTimeField(auto_now_add=False, auto_now=False, null = True)


