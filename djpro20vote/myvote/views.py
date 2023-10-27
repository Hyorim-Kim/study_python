from myvote.models import Question, Choice
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list': q_list}
    return render(request, 'display.html', context)

def DetailFunc(request, question_id):
    #print('question_id : ', question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)  # pk만 읽음
    # except Question.DoesNotExist:
    #     raise Http404("질문 항목 파일 없음")
    
    # get_object_or_404 : 없는 페이지에 대한 요청이 들어왔을 경우 404 오류를 발생시켜주는 메소드
    question = get_object_or_404(Question, pk=question_id)  # 16-19 라인과 같은 문장
    print(question.question_text)
    print(question.pub_date)
    print(question)  # question_text가 찍힘
    print('question.choice_set.all : ', question.choice_set.all())
    for cho in question.choice_set.all():
        print(cho.choice_text)
    
    return render(request, 'detail.html', {'question':question})

def VoteFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'err_msg':'1개의 항목을 선택하시오'})

    sel_choice.votes += 1
    sel_choice.save()  # 선택항목을 1씩 늘린 후 DB테이블 수정
    
    # urls.py에서 설정한 URL의 name이나, viewname을 통해서 통해서 다시 URL로 되돌릴 수 있다.
    print(reverse('results', args=(question.id,)))  # /gogo/1/results
    
    return HttpResponseRedirect(reverse('results', args=(question.id,)))


def ResultFunc(request, question_id):
    #return HttpResponse("bb")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question':question})

