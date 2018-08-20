from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complain(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    complainant = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE)
    #respondent = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE)
    comments = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title