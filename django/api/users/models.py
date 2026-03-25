from django.db import models

class User(models.Model):
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=30, blank=True)
  role = models.IntegerField(choices=[(0, "Admin"), (1, "User")], default=1)
  
  def __str__(self):
    return self.username