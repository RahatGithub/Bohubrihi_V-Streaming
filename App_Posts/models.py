from django.db import models
from django.contrib.auth.models import User 


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
        ('php', 'PHP'),
    ]
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=264, blank=True) 
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default=None)
    video_link = models.URLField(blank=True) 
    upload_date = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ['-upload_date',]  # try using the string '?' for random ordering
    
    def __str__(self):
        return f"{self.title} ({self.category})"