from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime

# Create your views here.
def mainFunc(request):
    imsi = "<div><h2>메인화면</h2></div>"  # html 형식의 문서를 전송
    return render(request, 'main.html', {'maintag':imsi})

def listFunc(request):
    data_all = BoardTab.objects.all().order_by('-gnum', 'onum') # gnum descending, onum ascending
    paginator = Paginator(data_all, 5)  # 한 페이지에 5개씩 출력
    # print(paginator) <django.core.paginator.Paginator object at 0x0000023A9294F8D0>
    
    # 페이지를 받는다.
    try:  # 클라이언트로 부터 페이지 요청을 받은 경우
        page = request.GET.get('page')
    except Exception as e:  # 클라이언트로 부터 페이지가 넘어오지 않는경우
        page = 1
        
    try:  # 페이지 정수 값을 받은 경우
        datas = paginator.page(page)
    except PageNotAnInteger:  # 페이지가 정수가 아닌 값을 받은 경우
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages())
    
    # 개별 페이지 표시 작업용
    # allpage = range(paginator.num_pages + 1)
    # print('allpage : ', allpage) allpage :  range(0, 4)
    return render(request, 'board.html', {'datas':datas})

def insertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        # 게시판 정보를 입력하고 요청 받았을 때
        try:
            gbun = 1
            datas = BoardTab.objects.all() # 전체 자료 읽는다.
            if datas.count() != 0: # 자료 있는 경우
                gbun = datas = BoardTab.objects.latest('id').id + 1
                print(gbun)
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('content'),
                bip = request.META['REMOTE_ADDR'], # request.META.get('REMOTE_ADDR')
                bdate = datetime.now(),
                readcnt=0,
                gnum=gbun,
                onum=0,
                nested=0,      
            ).save()
        except Exception as e:
            print('추가 에러 : ', e)
            return render(request, 'error.html')
        
    return redirect('/board/list')

def searchFunc(request):
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type, s_value)
        
        if s_type == 'title':
            # SQL의 like 문 : 칼럼명__contains
            datas_search = BoardTab.objects.filter(title__contains=s_value).order_by('-id')
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains=s_value).order_by('-id')
            
        paginator = Paginator(datas_search, 5)
        try:  # 클라이언트로 부터 페이지 요청을 받은 경우
            page = request.GET.get('page')
        except Exception as e:  # 클라이언트로 부터 페이지가 넘어오지 않는경우
            page = 1
        
        try:  # 페이지 정수 값을 받은 경우
            datas = paginator.page(page)
        except PageNotAnInteger:  # 페이지가 정수가 아닌 값을 받은 경우
                datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages())
        
        return render(request, 'board.html', {'datas':datas})

def contentFunc(request):
    pass

def updateFunc(request):
    pass

def deleteFunc(request):
    pass

