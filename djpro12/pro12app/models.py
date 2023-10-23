from django.db import models

# TABLE 만드는 곳
# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=20)
    mtel = models.CharField(max_length=30)
    maddr = models.CharField(max_length=50)
    # 아이디 대신에 이름으로 나오게 한다.
    def __str__(self):
        return self.mname
    
class Product(models.Model):
    pname = models.CharField(max_length=20)
    pprice = models.IntegerField()
    pmaker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) # Maker의 pk(id)키를 참조한다.