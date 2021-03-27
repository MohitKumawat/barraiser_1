from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    # Could add additional fields in here

    def __str__(self):
        return self.username
