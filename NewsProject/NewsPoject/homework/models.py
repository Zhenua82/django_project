from django.db import models


class Human(models.Model):
    Name = models.CharField(max_length=150)
    Last_name = models.TextField(blank=True)
    age = models.IntegerField()
    profession = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='media/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
