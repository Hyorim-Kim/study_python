from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created=True, primary_key=True)  # id 쓸거라 주석
    title = models.CharField(max_length=100)
    content = models.TextField()  # 자리수 안줘도 됨
    regdate = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class Meta:  # 정렬 방법 2
        # ordering=('title',)  # tuple type으로 기술
        ordering=('-id',)