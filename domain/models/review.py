from django.db import models

from domain.models import User


class Review(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)