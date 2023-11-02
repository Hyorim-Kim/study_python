# 시각화
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글처리 시 음수부호 깨짐 방지
"""
x = ['서울', '수원', '인천']
# x = ('서울', '수원', '인천')  # tuple도 가능
# x = {'서울', '수원', '인천'}  # set은 순서가 없어(indexing 안됨) 불가능
y = [5, 3, 7]
plt.xlim([-1, 3])  # 축 경계 지정
plt.ylim([-3, 10])
plt.plot(x, y)
plt.yticks(list(range(-3,11,3)))  # -3부터 11까지 증가치 3
plt.xlabel('지역명')
plt.ylabel('친구수')
plt.title('선 그래프')
plt.show()
"""

"""
# sin 곡선
x = np.arange(10)
y = np.sin(x)
print(x, y)
#plt.plot(x, y, 'bo')
#plt.plot(x, y, 'r+')
#plt.plot(x, y, 'go:', linewidth=3, markersize=10)
plt.plot(x, y, 'go--', linewidth=3, markersize=10)
plt.show()
"""

# hold : 복수의 차트 그리기 명령을 하나의 figure에 표현 할 수 있다.
x = np.arange(0, np.pi*3, 0.1)
#print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

"""
plt.figure(figsize=(10,5))
plt.plot(x, y_sin, c='r')
plt.scatter(x, y_cos, c='b')
plt.legend(['sine', 'cosine'], loc=1)
plt.show()
"""

# subplot : figure를 여러 개의 영역으로 나눠 차트를 그림
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('sine')
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()
