# tf.constanc() : 텐서를 직접 기억
# tf.Variable() : 텐서가 저장된 주소를 참조
import tensorflow as tf
import numpy as np

node1 = tf.constant(3, dtype=tf.float32)
node2 = tf.constant(4.0)
print(node1)
print(node2)
imsi = tf.add(node1, node2)
print(imsi)

print()
node3 = tf.Variable(3, dtype=tf.float32)
node4 = tf.Variable(4.0)
print(node3)
print(node4)
node4.assign_add(node3)
print(node4)

print()
a = tf.constant(5)
b = tf.constant(10)
c = tf.multiply(a, b)
result = tf.cond(a < b, lambda :tf.add(10, c), lambda :tf.square(a))
print('result : ', result.numpy())

print('\n-------')
v = tf.Variable(1)

@tf.function  # Graph 환경에서 처리가 됨
def find_next_func():
    v.assign(v + 1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)

find_next_func()
print(v.numpy())
print(type(find_next_func))
# <class 'function'>
# <class 'tensorflow.python.eager.polymorphic_function.polymorphic_function.Function'>  annotation 걸어줄때

print('func1 ---------------------------')
def func1():
    imsi = tf.constant(0)  # imsi = 0
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi

kbs = func1()
print(kbs.numpy(), ' ', np.array(kbs))

print('func2 ---------------------------')
imsi = tf.constant(0)  # 함수 밖에서 변수 선언
@tf.function
def func2():
    # imsi = tf.constant(0)  # imsi = 0  # 함수 내에서 변수 선언
    global imsi
    su = 1
    for _ in range(3):
        # imsi = tf.add(imsi, su)
        # imsi = imsi + su
        imsi += su  # constant는 제약 없음
    return imsi

kbs = func2()
print(kbs.numpy(), ' ', np.array(kbs))

print('func3 ---------------------------')
imsi = tf.Variable(0)
@tf.function
def func3():
    # imsi = tf.Variable(0)  # constant => Variable    error(autograph에서는 Variable은 함수 밖에서 선언)
    su = 1
    for _ in range(3):
        imsi.assign_add(su)  # Variable은 add말고 assign_add 사용
        # imsi = imsi + su  # error
        # imsi += su  # error
    return imsi

kbs = func3()
print(kbs.numpy(), ' ', np.array(kbs))

print('구구단 출력 -------------------')
# @tf.function  # 연산 속도 증진
def gugu1(dan):
    su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        # print(su)  # good(auto graph)
        # print(su.numpy())  # 형변환 error(auto graph)
        print('{} * {} = {}'.format(dan, su, dan*su))  # 서식 출력 안됨(auto graph)
        
gugu1(3)

print('\n------------------------')
# 내장함수 : numpy 지원 함수를 그대로 사용 +알파
# ... 중 reduce 함수 : 차원을 떨어뜨림
ar = [[1,2],[3,4]]
print(tf.reduce_sum(ar).numpy())
print(tf.reduce_mean(ar, axis=0).numpy())  # 열 방향
print(tf.reduce_mean(ar, axis=1).numpy())  # 행 방향

# one_hot encoding  종속변수에 사용, 성능이 더 잘나옴
print(tf.one_hot([0,1,2,0], depth=3))  # data를 배열로 생성. depth(열의 개수)는 배열 중 유니크한 값의 수만큼 부여
