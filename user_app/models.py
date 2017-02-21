from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Standard(User):

    def __str__(self):
        return User.first_name
