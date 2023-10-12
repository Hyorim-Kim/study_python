# Singer type의 객체 생성
class Singer:
    title_song = '와우 대한민국'  # public, 멤버변수
    
    def sing(self):
        msg = '노래는 '  # 지역변수
        print(msg, self.title_song)
    
    # ...