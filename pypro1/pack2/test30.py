from pack2.test30etc import ElecProduct
# ElecProduct를 상속받아 ElecTv와 ElecRadio 클래스를 생성

class ElecTv(ElecProduct):  # ElecProduct를 상속
    def volumeControl(self, volume):  # 오버라이딩
        self.volume += volume
        print('TV 소리 크기는 ' + str(self.volume))
        
class ElecRadio(ElecProduct):  # ElecProduct를 상속
    def showProduct(self):
        print('라디오 고유 메소드')
        
    def volumeControl(self, volume):  # 오버라이딩
        vol = volume
        self.volume += vol
        print('라디오 볼륨은 ', self.volume)
        
tv = ElecTv()  # 인스턴스 생성
tv.volumeControl(7)
tv.volumeControl(-3)
print()
radio = ElecRadio()  # 인스턴스 생성
radio.volumeControl(3)
radio.volumeControl(2)

print('~~~~~~~~~~~~~')  # 다형성
product = tv  # product 변수에 tv를 할당
product.volumeControl(10)  # tv의 volumeControl 메소드가 실행
print()
product = radio
product.volumeControl(10)
