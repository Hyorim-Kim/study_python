import pack2.test21singer

def process():
    jungkuk = pack2.test21singer.Singer()  # 생성자 호출, 인스턴스 됨
    print('타이틀 송 : ', jungkuk.title_song)
    jungkuk.sing()
    jungkuk.title_song = '정국 찬양가'
    jungkuk.co = '하이브'
    print('소속사가 ' + jungkuk.co + '인 가수의 노래 : ' + jungkuk.title_song)
    
    print()
    iu = pack2.test21singer.Singer()  # 생성자 호출
    print('타이틀 송 : ', iu.title_song)
    iu.sing()
    # print('소속사가 ' + iu.co + '인 가수의 노래 : ' + iu.title_song)  # co는 정국 instance만이 갖고 있기 때문에 에러
    print(id(pack2.test21singer.Singer), id(iu))  # 주소 다름
    
    print()
    bp = pack2.test21singer.Singer  # 객체의 주소를 넘겨받음 (singer와 bp는 주소가 같음), 새로운 타입의 객체가 만들어진 것이 아님(인스턴스화 X)
    print(id(pack2.test21singer.Singer), id(bp))  # 주소 같음
    # print(bp.sing())  # error, 왜? bp는 클래스 참조이며 인스턴스가 아니기 때문
    # sing 메서드는 클래스의 인스턴스에서 호출되어야 하며 클래스 참조에서 직접 호출할 수 없다
    print('타이틀 송 : ', bp.title_song)
    
if __name__ == '__main__':
    process()
