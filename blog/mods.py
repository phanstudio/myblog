from django.db import models
from .models import Post

class Image(models.Model):
    post = models.ForeignKey('post', on_delete=models.CASCADE, null= True)
    image = models.ImageField(upload_to='img/')

Post.images = models.ManyToManyField(Image, blank=True, related_name='posts')