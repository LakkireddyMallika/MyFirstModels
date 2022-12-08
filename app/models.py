from django.db import models
# Create your models here.
class Topic(models.Model):
    Topic_Name=models.CharField(max_length=200,primary_key=True)

class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()  