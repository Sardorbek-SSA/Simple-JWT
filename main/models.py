from django.db import models
from django.contrib.auth.models import User

class Toy(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='toys')
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    