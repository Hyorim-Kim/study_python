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
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))  # 해당 아이디의 자료
    data.readcnt = data.readcnt + 1  # 읽음
    data.save()  # 업데이트가 이루어짐 -> 조회수 갱신
    return render(request, 'content.html', {'data':data, 'page':page})

def updateFunc(request):
    if request.method == 'GET':
        try:
            data = BoardTab.objects.get(id=request.GET.get('id'))  # 수정할 자료 읽기
            return render(request, 'update.html', {'data':data})
        except Exception as e:
            print('수정 자료 읽기 오류 : ', e)
            return render(request, 'error.html')
    elif request.method == 'POST':
        try:
            updata = BoardTab.objects.get(id=request.POST.get('id'))  # 수정할 자료 읽기
            # 비밀번호는 수정에서 제외
            if updata.passwd == request.POST.get('up_passwd'):  # 비밀번호 확인
                updata.name = request.POST.get('name')
                updata.mail = request.POST.get('mail')
                updata.title = request.POST.get('title')
                updata.cont = request.POST.get('content')
                updata.save()
                return redirect('/board/list')  # 수정 후 목록 보기
            else:
                return render(request, 'update.html', {'updata':updata, 'upmsg':"비밀번호 불일치!"})
            
        except Exception as e:
            print('수정 자료 처리 오류 : ', e)
            return render(request, 'error.html')

def deleteFunc(request):
    if request.method == 'GET':
        try:
            deldata = BoardTab.objects.get(id=request.GET.get('id'))
            return render(request, 'delete.html', {'data':deldata})
        except Exception as e:
            print('삭제 자료 읽기 오류 : ', e)
            return render(request, 'error.html')
    elif request.method == 'POST':
        try:
            deldata = BoardTab.objects.get(id=request.POST.get('id'))  # 삭제할 때 post 방식을 썼기 때문에 두번작성***
            if deldata.passwd == request.POST.get('del_passwd'):
                deldata.delete()
                return redirect('/board/list')  # 삭제 후 목록보기
            else:
                return render(request, 'error.html')
        except Exception as e:
            print('삭제 자료 처리 오류 : ', e)
            return render(request, 'error.html')

