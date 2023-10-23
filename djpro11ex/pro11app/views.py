from django.shortcuts import render, redirect
from pro11app.models import Family
from django.db.models.aggregates import Avg

# Create your views here.
def RegisterFunc(request):
    return render(request, 'register.html')

def ListFunc(request):
    fdatas = Family.objects.all()  # 클래스명.objects.all()
    average_age = fdatas.aggregate(avg_age=Avg('age'))['avg_age']
    return render(request, 'list.html', {'fdatas': fdatas, 'average_age': average_age})

def InsertOkFunc(request):
    if request.method == 'POST':
        Family(
            name = request.POST['name'],  # 변수명은 테이블의 칼럼명, 괄호 안은 파라미터명과 일치해야 함
            age = request.POST['age'],
            tel = request.POST['tel'],
            gen = request.POST['gen'],
        ).save()
        
        # 수정
        # Guest(
        #     g = Guest.objects.get(id=수정할번호)
        #     g.title = request.POST['title'],  # 변수명은 테이블의 칼럼명, 괄호 안은 파라미터명과 일치해야 함
        #     g.content = request.POST['content'],
        # ).save()
        
        # 삭제
        # g = Guest.objects.get(id=삭제할번호)
        # g.delete()
        
    # return HttpResponseRedirect("/guest/select")  # 클라이언트 화면에서 전송받아야 함, 아래 문장과 같음
    return redirect ("list.html")  # 추가 후 목록보기
        