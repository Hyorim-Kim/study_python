from django.shortcuts import render
from pro8app.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    datas = Article.objects.all()  # Django ORM
    print(datas)  # <QuerySet []>  select의 결과를 QuerySet type으로 반환한다. ** sql문을 직접 쓰면 QuerySet type이 아님
    print(datas[0].name)
    return render(request, 'list.html', {'datas':datas})


