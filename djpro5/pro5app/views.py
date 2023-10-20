from django.shortcuts import render

# Create your views here.
def MainFunc(request):
    return render(request, 'index.html')

def Herit1Func(request):
    return render(request, 'kbs1.html')

def Herit2Func(request):
    return render(request, 'kbs2.html')
