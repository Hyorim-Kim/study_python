from django.shortcuts import render, redirect
from pro11app.models import Family
from django.db.models.aggregates import Avg
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'register.html')

def ListFunc(request):
    fdatas = Family.objects.all()
    average_age = fdatas.aggregate(avg_age=Avg('age'))['avg_age']
    return render(request, 'list.html', {'fdatas': fdatas, 'average_age': average_age})

def InsertFunc(request):
    return render(request, 'register.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Family(
            name = request.POST['name'],  # 변수명은 테이블의 칼럼명, 괄호 안은 파라미터명과 일치해야 함
            age = request.POST['age'],
            tel = request.POST['tel'],
            gen = request.POST['gen'],
        ).save()      
    #return redirect ("list.html")  # 추가 후 목록보기
    return HttpResponseRedirect("/family/select")
        