from django.db import models

#iha ->  İHA Features: id(AutoField), Brand(Charfield), Model(Charfield), Weight(NumericField), Category(Charfield) etc.
# Create your models here.
class IHA(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    weight = models.IntegerField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.brand


class Lessees(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username

class Orders(models.Model):
    id    = models.AutoField(primary_key=True)
    user_id  = models.IntegerField()
    order_id = models.IntegerField()
    
    def __str__(self):
        return self.id