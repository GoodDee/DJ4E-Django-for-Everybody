from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    region = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.region   
    
class State(models.Model):
    state = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.state   

class Iso(models.Model):
    iso = models.CharField(max_length=128)
    
    def __str__(self) :
        return self.state   


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null = True)
    justification = models.TextField(null = True)
    year = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name