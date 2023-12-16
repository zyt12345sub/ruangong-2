from django.db import models


# Create your models here.
class Reporter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=20)


class Pothole(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    size = models.IntegerField()  # scale of 1 to 10
    location = models.CharField(max_length=200)
    reporter_id = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Workorder(models.Model):
    id = models.AutoField(primary_key=True)
    pothole_id = models.ForeignKey(Pothole, on_delete=models.CASCADE)
    crew_id = models.IntegerField()
    crew_number_of_people = models.IntegerField()
    equipment = models.CharField(max_length=200)
    repair_hour = models.DecimalField(max_digits=5, decimal_places=2)
    hole_status = models.CharField(max_length=20)
    material = models.DecimalField(max_digits=5, decimal_places=2)
    cost_of_repair = models.DecimalField(max_digits=15, decimal_places=2)


class DamageFile(models.Model):
    id = models.AutoField(primary_key=True)
    pothole_id = models.ForeignKey(Pothole, on_delete=models.CASCADE)
    reporter_id = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    type_of_damage = models.CharField(max_length=50)
    dollar_amount = models.DecimalField(max_digits=15, decimal_places=2)
