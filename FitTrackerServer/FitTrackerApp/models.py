from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    # Add more fields as needed

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('userprofile_detail', args=[str(self.id)])


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    successful = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise_detail', args=[str(self.id)])
