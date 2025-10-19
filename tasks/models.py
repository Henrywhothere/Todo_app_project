from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def mark_done(self):
        self.completed = True
        self.save()

