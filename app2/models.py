from django.db import models

# Create your models here.

class new_one(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=5)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
