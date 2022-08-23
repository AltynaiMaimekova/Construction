from django.db import models


class Block(models.Model):
    number = models.IntegerField()
    cost_per_sqm = models.IntegerField()
    entrances = models.IntegerField()
    floors = models.IntegerField()
    number_apartments = models.IntegerField()

    def __str__(self):
        return f'block {self.number} with {self.entrances} entrances'


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('Sold', 'Выкуп'),
        ('Partially sold', 'Выкуп не до конца'),
        ('Separated', 'Расторгнуто'),
        ('Not sold', 'Не продано'),
    ]
    surname = models.CharField(max_length=50, null=True, blank=True)
    date_purchase = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Not sold')
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    squire = models.IntegerField()

    def __str__(self):
        return f'apartment {self.squire} squire meters'


