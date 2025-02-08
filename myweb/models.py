from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=now)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=now)
    amount = models.BigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # kheili gaydi
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
