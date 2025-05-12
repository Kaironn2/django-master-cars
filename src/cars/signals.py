from django.db.models import Sum
from django.db.models.signals import (
    post_delete,
    post_save,
)
from django.dispatch import receiver

from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = (
        Car.objects.aggregate(total_amount=Sum('price'))['total_amount'] or 0
    )
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value,
    )


@receiver(post_save, sender=Car)
def post_save_handler(sender, instance, created, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def post_delete_handler(sender, instance, **kwargs):
    car_inventory_update()
