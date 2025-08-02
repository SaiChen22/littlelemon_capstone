from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : ${self.price}'
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.name} - {self.booking_date}'
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
