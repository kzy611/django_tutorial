import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone


class Record(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    expense_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField()
    category = models.ForeignKey('expenses.Category', on_delete=models.CASCADE, related_name='records')
    payment = models.ForeignKey('expenses.Payment', on_delete=models.CASCADE, related_name='records')
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.expense_date.strftime('%Y-%m-%d') + ': ' + str(self.amount) + ': ' + self.note

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
