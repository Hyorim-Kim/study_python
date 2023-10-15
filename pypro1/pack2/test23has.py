# 클래스의 포함관계 : 국인이네 냉장고(객체)에 음식(객체) 담기

class Fridge:
    isOpened = False  # 냉장고 문 개폐 여부
    foods = []  # 냉장고에 담긴 음식을 저장하는 리스트
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:  # 문이 열려 있을 때만
            self.foods.append(thing)  # 포함관계  # list 에 데이터 넣을땐 append            
            print('냉장고 속에 음식 담기 완료')
            self.list()
        else:
            print('냉장고 문이 닫혀서 음식을 담을 수 없어요')
            
    def close(self):
        self.isOpened = False
        print('냉장고 문  꼭 닫기')

    def list(self):  # 내용물 보기
        for f in self.foods:
            print('-', f.name, f.expiry_date)
        print()

# 음식물 클래스
class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

# 실행
fr = Fridge()  # 생성자 호출, 내용이 없는 생성자
apple = FoodData('사과', '2023-11-05')
fr.put(apple)
fr.open()
fr.put(apple)
fr.close()
print('---')
cola = FoodData('콜라', '2025-10-05')
fr.open()
fr.put(cola)
fr.close()
