from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class word(models.Model):
    polish = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    level_id = models.IntegerField()


class player(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    highscore = models.IntegerField()
    level_id = models.IntegerField()
