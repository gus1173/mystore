from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    def avg_rating(self):
        rating=self.reviews_set.all().values_list('ratings',flat=True)
        if rating:
            return sum(rating)/len(rating)
        else:
            return 'No ratings'
    def review_count(self):
        rating=self.reviews_set.all().values_list('ratings',flat=True)
        if rating:
            return len(rating)
        else:
            return 'No reviews'
    
    def __str__(self):
        return self.name

class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Products = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    Products = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comments =models.CharField(max_length=200)

    def __str__(self):
        return self.comments
    