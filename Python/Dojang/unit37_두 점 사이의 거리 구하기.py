# 클래스를 활용하여 2차원 평면에서 위치를 표현한 후 두 점 사이의 거리 구하기

# 클래스로 점 구현하기
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p1 = Point2D(30, 20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
 
print('p1: {} {}'.format(p1.x, p1.y))    # 30 20
print('p2: {} {}'.format(p2.x, p2.y))    # 60 50

# 피타고라스의 정리로 두 점 사이의 거리 구하기
import math
a = p1.x - p2.x
b = p2.y - p1.y
c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(c)

## nametuple 사용하기
# 클래스 = collections.nametuple('자료형이름', ['요소 이름1', '요소 이름2'])
import collections

Point2D = collections.namedtuple('Point2D', ['x','y'])
p3 = Point2D(x = 10, y = 20)
p4 = Point2D(x = 30, y = 40)
print(type(p3), p4.x, p4.y, p4)

## 연습문제 : 사각형의 넓이 구하기
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
rect = Rectangle(20,20,40,30)
a = abs(rect.x1 - rect.x2)
b = abs(rect.y1 - rect.y2)
area = a * b
print(area)

## 심사문제

class Point2D :
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
lens = []
for i in range((len(p) - 1)):
    x = math.pow(p[i].x - p[i+1].x , 2)
    y = math.pow(p[i].y - p[i+1].y , 2)
    length = math.sqrt(x + y)
    lens.append(length)
length = sum(lens)
print(length)  

'''
덕 타이핑이란?
실제 타입(클래스)은 상관하지 않고, 구현된 메서드로만 판단하는 방식. 

믹스인이란?
다른 클래스에서 사용할 수 있도록 공통적인 메서드를 모아 놓은 클래스

'''