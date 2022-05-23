from django.db import models



class Home(models.Model):
    sale = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bedroom = models.IntegerField()
    bath = models.IntegerField()
    square_feet = models.IntegerField()
    photo = models.ImageField()
