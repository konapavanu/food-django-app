from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    def __str__(self):
       return  self.item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField()
    item_desc=models.CharField()
    item_price=models.IntegerField()
    item_image=models.CharField(default="https://plakarestaurant.ca/wp-content/themes/twentytwentythree-child/img/food-placeholder.png")

def get_absolute_url(self):
    return reverse("food:detail",kwargs={"pk":self.pk})