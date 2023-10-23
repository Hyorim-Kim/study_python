from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    tel = models.CharField(max_length=20)
    gen = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name
    
    class Meta:  # 정렬 방법 2
        ordering=('id',)