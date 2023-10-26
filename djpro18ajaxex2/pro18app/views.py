# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})

def calculate_price(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        quantity = int(request.POST.get('quantity'))
        
        # 여기에서 상품 가격을 가져오고 가격을 계산하는 로직을 추가해야 해.
        # 그리고 결과를 JsonResponse로 반환해야 해.

    return JsonResponse({'error': 'Invalid request'})
