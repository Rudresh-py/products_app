from django.db import models


# Create your models here.
class Product(models.Model):
    name_txt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    pub_date = models.DateField()

    def __str__(self):
        return self.name_txt



class Rating(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def __int__(self):
        return self.rate
