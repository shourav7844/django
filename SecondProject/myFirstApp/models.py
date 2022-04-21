from django.db import models

# Create your models here.

class registration(models.Model):
    User_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=8)
    Email_address = models.EmailField(max_length = 50, blank = True, unique = True)
    def __str__(self):
        return f"{self.Name}"