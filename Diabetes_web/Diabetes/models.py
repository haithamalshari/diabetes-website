from django.db import models

# Create your models here.
class Dataset(models.Model):
    age = models.IntegerField(null=False)
    bmi = models.IntegerField(null=False)
    wrkout = models.IntegerField(null=False)
    alcol = models.IntegerField(null=False)
    gender = models.IntegerField(null=False)
    bp = models.IntegerField(null=False)
    chol = models.IntegerField(null=False)
    suger = models.IntegerField(null=False)
    fat = models.IntegerField(null=False)
    race = models.IntegerField(null=False)
    marital = models.IntegerField(null=False)
    edu = models.IntegerField(null=False)
    smoke = models.IntegerField(null=False)
    preg = models.IntegerField(null=False)
    pred = models.IntegerField(null=False)
    feed = models.IntegerField(default=3,null=False)
