from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
