from django.shortcuts import render
from pro9app.models import Article

# Create your views here.
def Main(request):
    return render(request, 'index.html')

def DbShow(request):
    datas = Article.objects.all()
    print(datas)
    print(datas[0].irum)
    return render(request, 'list.html', {'datas':datas})
