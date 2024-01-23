from django.db import models

# Create your models here.


class StuInfo(models.Model):
    
    roll = models.IntegerField()
    Name = models.CharField(max_length = 200)
    Address = models.TextField(max_length=300)
    
    
    