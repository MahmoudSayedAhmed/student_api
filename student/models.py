from django.db import models

# Create your models here.
class Students(models.Model):
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    

    class Meta:
        ordering = ('username',)