from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

ACTIVITY = (
  ('S', 'Save a kitten in Tree'),
  ('F', 'Fight a villain'),
  ('T', 'Train')
)

class Workout(models.Model):
  name = models.CharField(max_length=50)
  weight = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('workout-detail', kwargs={'pk': self.id})

# Create your models here.
class Hero(models.Model):
  name = models.CharField(max_length=100)
  power = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  workouts = models.ManyToManyField(Workout)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('hero-detail', kwargs={'hero_id': self.id})
  
  def training_for_today(self):
    return self.training_set.filter(date=date.today()).count() >= len(ACTIVITY)
  
class Training(models.Model):
  date = models.DateField('Training Date')
  activity = models.CharField(
    max_length=1,
    choices=ACTIVITY,
    default=ACTIVITY[0][0]
  )
  hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_activity_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']