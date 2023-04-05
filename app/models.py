from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=15)
    position = models.CharField(max_length=2)


class Meta:
    verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title
