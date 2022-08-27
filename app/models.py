from django.db import models


class VarGroup(models.Model):
    title= models.CharField(max_length=100, default='')

class Var(models.Model):
    text= models.CharField(max_length=100, default='')
    num= models.IntegerField(default=0)
    bit= models.BooleanField(default=False)
    date= models.DateField(auto_now=True)
    group= models.ForeignKey(VarGroup, on_delete=models.CASCADE, null=True)
