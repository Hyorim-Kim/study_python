import random
from django.shortcuts import render

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
    if request.method == 'POST':
        # 정수 난수 발생 (1 이상 100 이하)
        random_number = random.randint(1, 100)
    
        # 난수가 짝수면 "남자", 홀수면 "여자"
        gender = "남자" if random_number % 2 == 0 else "여자"
    
        # 결과를 템플릿에 전달하여 출력
        context = {'gender': gender}
        return render(request, 'show.html', context)
    else:
        return render(request, 'show.html', context)
