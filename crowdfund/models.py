from django.db import models
from ..autentikasi.models import Account

class Crowdfund(models.Model):
    fundraiser = models.ForeignKey(Account, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    collected = models.PositiveIntegerField()
    target = models.PositiveIntegerField()
    deadline = models.DateTimeField()

class Donation(models.Model):
    donator = models.ForeignKey(Account, on_delete = models.CASCADE)
    crowdfund = models.ForeignKey(Crowdfund, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField()
    comment = models.TextField(blank=True)