from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Delete a post once the author gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20,default="")
    post_image = models.ImageField(default='featured-image.png', upload_to='post_featured_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})