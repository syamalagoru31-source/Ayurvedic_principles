from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    prakriti = models.CharField(max_length=50)  # Vata, Pitta, Kapha

    def __str__(self):
        return self.user.username


class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    symptoms = models.TextField()
    prevention_tips = models.TextField()

    def __str__(self):
        return self.name


class Remedy(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    remedy_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    preparation = models.TextField()
    benefits = models.TextField()

    def __str__(self):
        return self.remedy_name


class HealthTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title