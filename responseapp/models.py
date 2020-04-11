from django.db import models

class user:
    email=str
    name=str
    user_type=str

class doctor:
    email=str
    name=str
    hospital_name=str
    eth_address=str
    doctor_type=str

class patient:
    email=str
    ethaddress=str
    name=str
    number=str

class medicals:
    email=str
    medname=str
    ownername=str


# class Country(models.Model):
#     name = models.CharField(max_length=30)

# class City(models.Model):
#     name = models.CharField(max_length=30)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     population = models.PositiveIntegerField()

