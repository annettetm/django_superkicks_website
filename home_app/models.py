from django.db import models

# Create your models here.
class product(models.Model):
    image=models.ImageField(upload_to="picture")
    name=models.CharField(max_length=255)
    price=models.IntegerField()