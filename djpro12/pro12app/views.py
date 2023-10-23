from django.shortcuts import render
from pro12app.models import Maker, Product
from django.db.models.aggregates import Count,Avg,Sum,StdDev

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    
    # ORM 함수 연습
    print(products)  # <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>]>
    print(products.values_list())  # <QuerySet [(1, '누텔라 비스킷', 10000, 2), (2, '슬리퍼', 15000, 1), (3, '너구리', 1000, 3)]>
    
    print(Product.objects.all().count())  # 3
    print(products.aggregate(Count('pprice')))  # {'pprice__count': 3}
    print(products.aggregate(Sum('pprice')))  # {'pprice__sum': 26000}
    print(products.aggregate(Sum('pprice'))['pprice__sum'])  # 26000
    print(products.aggregate(Avg('pprice')))
    print(products.aggregate(StdDev('pprice')))
    
    aa = products.filter(pname='슬리퍼')  # 걸러보기
    print(aa)
    for a in aa.values_list():
        print(a)
        
    print()
    aa = products.exclude(pname='슬리퍼')  # 제외하기
    print(aa)
    for a in aa.values_list():
        print(a)
    
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(pmaker_name=mid)  # pmaker_name : pk를 참조
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})
