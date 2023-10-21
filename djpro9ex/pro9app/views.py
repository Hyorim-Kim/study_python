from django.shortcuts import render
from pro9app.models import Article

# Create your views here.
def Main(request):
    return render(request, 'index.html')

def DbShow(request):
    datas = Article.objects.all()  # DB에서 모든 Article 객체를 가져와 datas 변수에 할당
    print(datas)
    print(datas[0].irum)
    return render(request, 'list.html', {'datas':datas})
    # list.html 템플릿에 datas를 전달하여 렌더링한 결과를 클라이언트에 반환
