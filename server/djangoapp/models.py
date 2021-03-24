from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.name + ' ' + self.description

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    dealer_id = models.IntegerField()

    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'WAGON')
    ]
    car_type = models.CharField(null=False, max_length=50, choices=TYPE_CHOICES)
    year = models.DateField(null=False, default=now)

    def __str__(self):
        return str(self.carmake) + ' ' + self.name + ' ' + str(self.dealer_id) + ' ' + self.car_type + ' ' + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
