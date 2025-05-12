from django.db import models

from cars.validators import year_validator


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='cars'
    )
    factory_year = models.IntegerField(
        blank=True, null=True, validators=year_validator
    )
    model_year = models.IntegerField(
        blank=True, null=True, validators=year_validator
    )
    plate = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    photo = models.ImageField(upload_to='cars/photos/', blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField(default=0)
    cars_value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Car Inventory'
        verbose_name_plural = 'Car Inventories'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
