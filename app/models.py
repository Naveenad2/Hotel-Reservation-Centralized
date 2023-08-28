from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    
    connection = models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone_number =models.IntegerField()

    def __str__(self) :
        return self.name
    

class Location(models.Model):

    location_name = models.CharField(max_length=50)
    pin = models.IntegerField(max_length=50)
    photo=models.ImageField(upload_to='./static/images')

    def __str__(self) :
        return self.location_name
    

class Hotels(models.Model):

    hotel_name = models.CharField(max_length=50)
    Select_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()

    discription = models.CharField(max_length=1000)
    photo = photo=models.ImageField(upload_to='./static/images')
    rent_per_day = models.IntegerField()
    
    def __str__(self) :
        return self.hotel_name


class Bookings(models.Model):

    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    user = models.ForeignKey(Customer,on_delete=models.CASCADE)

    start_date = models.CharField(max_length=50)

    end_date = models.CharField(max_length=50)
    number_of_days = models.IntegerField()
    total_amount_paid = models.IntegerField()

    def __str__(self) :
        return self.user.name
    