from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class RegListing(models.Model):
    reguser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
