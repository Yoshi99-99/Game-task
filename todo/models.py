from django.db import models
from django.utils import timezone

# Create your models here.
class Daily_mission(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50)
    description = models.TextField(verbose_name='詳細説明', blank=True)
    deadline = models.DateField(verbose_name='締め切り', default=timezone.now)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Weekly_mission(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50)
    description = models.TextField(verbose_name='詳細説明', blank=True)
    deadline = models.DateField(verbose_name='締め切り', default=timezone.now)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Nomal_mission(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=50)
    description = models.TextField(verbose_name='詳細説明', blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title