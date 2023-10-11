# 그래픽을 지원하는 외부 모듈로 turtle
import turtle

"""
def gogo():
    a = turtle.Pen()  # 그림 그리기 용 펜 생성
    a.forward(100)  # 오른쪽으로 수평 이동
    a.right(90)  # 시계방향으로 90도 회전
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    input()
    
if __name__ == "__main__":  # 응용프로그램에서 메인모듈임을 나타내는 방법, 권장 *
    gogo()
"""
     
import turtle

ak = turtle.Turtle()
ak.getscreen().bgcolor("#994444")
ak.speed(10)

ak.penup()
ak.goto((-200,100))
ak.pendown()

def star(turtle,size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()

star(ak,300)

turtle.done()
