from django.shortcuts import render
import MySQLdb
from pro13app.models import Sangdata

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3307,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    '''
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from sangdata"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)  # ((1, '장갑', 3, 10000), (2, '벙어리장갑', 3, 12000), ...
        print(type(datas))  # <class 'tuple'>
        
        return render(request, 'list.html', {'datas':datas})
    except Exception as err:
        print('에러 : ', err)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    '''
    
    datas = Sangdata.objects.all()
    print(datas)  # <QuerySet [<Sangdata: Sangdata object (1)>, <Sangdata: Sangdata object (2)>, ...
    print(type(datas))  # <class 'django.db.models.query.QuerySet'>
    return render(request, 'list.html', {'datas':datas})

def InsertFunc(request):
    pass

def InsertOkFunc(request):
    pass

def UpdateFunc(request):
    pass

def UpdateOkFunc(request):
    pass

def DeleteFunc(request):
    pass
