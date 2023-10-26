from django.shortcuts import render
import json
from django.http.response import HttpResponse
from doc.pycurl.examples.quickstart.response_headers import content_type

# dict data
lan = {
    'id':123,
    'name':'파이썬',
    'history':[
        {'date':'2023-10-25', 'exam':'basic'},
        {'date':'2023-10-26', 'exam':'django'},
    ]
}

def testFunc():  # 일반 함수
    print(type(lan))  # <class 'dict'>
    # Python object(dict, list, tuple 등)을 문자열로 변환 : Json encoding
    # Json 모양의 문자열을 Python object(dict)로 변환 : Json decoding
    jsonString = json.dumps(lan)  # Json encoding
    print(jsonString)
    print(type(jsonString))  # <class 'str'>
    jsonString = json.dumps(lan, indent=4)  # 들여쓰기
    print(jsonString)
    # print(jsonString['name'])  # 문자열이기 때문에 error
    print('***' * 10)
    
    dictData = json.loads(jsonString)  # Json decoding'
    print(dictData)
    print(type(dictData))  # <class 'dict'>
    print(dictData['name'])  # 파이썬
    for h in dictData['history']:
        print(h['date'], h['exam'])
    
    
# Create your views here.
def MainFunc(request):
    testFunc()
    return render(request, 'abc.html')


def Func1(request):
    msg = request.GET.get('msg')
    msg = "nice " + msg
    print(msg)
    context = {'key':msg}
    # json encoding (json 모양을 유지하며 문자열로 바뀜)
    return HttpResponse(json.dumps(context), content_type="application/json")


def Func2(request):
    mydata = [
        {'irum':'tom1','nai':22},
        {'irum':'tom2','nai':12},
        {'irum':'tom3','nai':2}
    ]  # list 안 dict
    return HttpResponse(json.dumps(mydata), content_type="application/json")

