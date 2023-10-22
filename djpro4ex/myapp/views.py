from random import randint
from django.shortcuts import render

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
    i = randint(1, 100)
    if i%2 == 0:
        gen = '남자'
        img = "/static/images/boy.jpg"
    else:
        gen = '여자'
        img ="/static/images/girl.jpg"
    return render(request, 'show.html', {'gen':gen, 'img':img})
