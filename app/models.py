from django.db import models

class Var(models.Model):
    text= models.CharField(max_length=100, default='')
    num= models.IntegerField(default=0)
    bit= models.BooleanField(default=False)
    date= models.DateField(auto_now=True)
