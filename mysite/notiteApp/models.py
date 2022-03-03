from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    IMPORTANCE_CHOICES = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=3)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Note, self).save(*args, **kwargs)

