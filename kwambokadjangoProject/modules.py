from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    disease = models.CharField(max_length=30, blank=False, null=False)
    referencenum = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField()
    dosage = models.IntegerField()
    price = models.IntegerField()


def __str__(self):
    return self.name
