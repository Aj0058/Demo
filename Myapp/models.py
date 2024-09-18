from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=200)
    Message = models.TextField()
    
    def __str__(self):
        return self.Name

class Feedback(models.Model):
    Name2 = models.CharField(max_length=200)
    Email2 = models.EmailField()
    Phone2 = models.CharField(max_length=200)
    Product2 = models.CharField(max_length=200)
    Message2 = models.TextField()

    def __str__(self):
        return self.Name2

