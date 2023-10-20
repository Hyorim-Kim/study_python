from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')  # forwarding

def selectOsFunc(request):
    #print('request.GET : ', request.GET)  # request.GET :  <QueryDict: {}>
    if "favorite_os" in request.GET:
        print(request.GET["favorite_os"])  #GET 방식의 요청값 출력
        request.session["f_os"] = request.GET["favorite_os"]  # session key를 부여  # session에 값 저장
        # return HttpResponseRedirect("showos")  # redirect
        return redirect("/showos")  # redirect
    else:
        return render(request, 'selectos.html')  # forwarding


def showOsFunc(request):
    #print("showOsFunc 도착")
    dict_context = {}
    
    if "f_os" in request.session:  # session 읽기, session 값 중 f_os가 있으면
        print('유효시간 : ', request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]  # key가 갖고 있는 값 넘김
        dict_context['message'] = "그대가 선택한 운영체제는 %s" % request.session["f_os"]
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = "운영체제를 선택하지 않았군요"
        
        
    # del request.session["f_os"]  # 특정 key를 가진 session을 삭제
    request.session.set_expiry(5)  # 5초만 유지
    
    return render(request, 'show.html', dict_context)  # key value 형식으로 넘김
