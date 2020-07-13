from django.db import models

# Create your models here.


class Checkin(models.Model):

    GENDER_CHOICES = [
        ('m', 'MALE'),
        ('f', 'FEMALE'),
        ('o', 'OTHER'),
    ]

    passport = models.ImageField()
    designation = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=False)
    address = models.TextField(max_length=100)
    phone_number = models.IntegerField()
    email_address = models.EmailField(max_length=35)
    nationality = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    amount = models.IntegerField()
    room_number = models.IntegerField()
    checkin_date = models.DateTimeField()

    def __str__(self):
        return self.first_name
