from django.db import models

# Create your models here.


class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount=models.FloatField()
    category=models.CharField(max_length=200)
    dec=models.TextField()
    img=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
    

class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Zip=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name