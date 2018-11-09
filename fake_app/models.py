from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)
    website_name = models.CharField(max_length=264, unique=True)
    website_url = models.URLField(unique=True)
    access_date = models.DateField()
