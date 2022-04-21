from django.db import models

class registration(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    password = models.CharField(max_length=32, null=True, blank=True)
    email_address = models.EmailField(max_length=60,null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registration'
        ordering = ['email_address']
        db_table = 'registration'

    def __str__(self):
        return f"{self.name}"
