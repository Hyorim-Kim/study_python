from django.shortcuts import render, redirect
from pro10app.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    # print('성공')
    print(Guest.objects.filter(title__contains='연습'))  # filter : where 조건과 비슷한 개념
    print(Guest.objects.filter(title='연습'))
    print(Guest.objects.get(id=1))  # 한개 읽을 때는 filter 대신 get 사용
    
    # select * from pro10app_guest  아래 문장과 같음
    gdatas = Guest.objects.all()  # 클래스명.objects.all()
    # gdatas = Guest.objects.all().order_by('-id')  # 정렬 방법 1
    # gdatas = Guest.objects.all().order_by('title','-id')   # title ascend, id descend
    # gdatas = Guest.objects.all().order_by('-id')[0:2]  # 레코드 제한
    return render(request, 'list.html', {'gdatas':gdatas})  # gdatas라는 키에 gdatas 달고감

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        # print(request.POST.get('title'))
        # print(request.POST['title'])
        # insert into pro10app_guest(...
        Guest(
            title = request.POST['title'],  # 변수명은 테이블의 칼럼명, 괄호 안은 파라미터명과 일치해야 함
            content = request.POST['content'],
            regdate = datetime.now()
            # regdate = timezone.now()
        ).save()
        
        # 수정
        # Guest(
        #     g = Guest.objects.get(id=수정할번호)
        #     g.title = request.POST['title'],
        #     g.content = request.POST['content'],
        # ).save()
        
        # 삭제
        # g = Guest.objects.get(id=삭제할번호)
        # g.delete()
        
    # return HttpResponseRedirect("/guest/select")  # 클라이언트 화면에서 전송받아야 함, 아래 문장과 같음
    return redirect ("/guest/select")  # 추가 후 목록보기
        