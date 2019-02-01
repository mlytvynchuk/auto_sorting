from django.contrib.auth.models import User
from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    price = models.FloatField()
    year = models.IntegerField()

    # will be generated depends on year of car
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s - %s" % (self.brand, self.model)

    def save(self, *args,**kwargs):

        if 0 < self.year < 1990:
            self.category = Category.objects.get(id=1)

        elif 1990 <= self.year < 2000:
            self.category = Category.objects.get(id=2)

        elif 2000 <= self.year < 2010:
            self.category = Category.objects.get(id=3)

        elif self.year >= 2010:
            self.category = Category.objects.get(id=4)

        super(Car,self).save(*args,**kwargs)

