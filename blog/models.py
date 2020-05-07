from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=120)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='blog/images')
    content = models.TextField(blank=True)
