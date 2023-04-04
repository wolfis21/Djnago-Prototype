from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    desc = models.TextField()
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title