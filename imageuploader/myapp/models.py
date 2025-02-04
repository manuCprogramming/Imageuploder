from django.db import models

# Create your models here.
class Image(models.Model):
 name = models.CharField(max_length=100)
 photo = models.ImageField(upload_to="mediamyimage")
 date = models.DateTimeField(auto_now_add=True)
 description = models.TextField()
 new_field = models.IntegerField(default=0)