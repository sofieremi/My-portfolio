from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()


class Human(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.IntegerField()
    registration_date = models.DateField()
