from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content  = models.TextField()
    number = models.CharField(max_length=10)
   