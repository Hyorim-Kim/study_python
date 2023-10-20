from django.db import models

# Create your models here.
# 논리적 테이블으로 물리적 테이블과 매핑된다. jpa의 entity와 비슷한 개념
# 칼럼을 추가, 삭제, 수정하면 migrations를 삭제 후 Django - make Migrations 하기
class Article(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
