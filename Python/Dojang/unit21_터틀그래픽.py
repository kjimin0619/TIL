'''
21. 터틀 그래픽

'''

import turtle as t

# .shape() : 거북이 모양 설정. 아무것도 지정하지 않으면 화살표 모양
'''
터틀 모양 설정하기
arrow, turtle, circle, square, triangle, classic 등 지정가능
t.shape() 하면 현재 모양을 알아낼 수 있음
'''
t.shape('turtle')
t.forward(100)
t.right(90) # 거북이 방향 변경
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100) # 정사각형 그리기 완성

# 다각형 그리고 색칠하기
t.reset()
t.right(90)
n = int(input()) # 사용자 입력받기

# 다각형 색칠 준비
t.color('skyblue') # 색깔 지정. RGB로도 지정가능(#000000 : 검정)
t.begin_fill() # 색칠할 영역 시작

# 다각형 그리기
for i in range(n):
    t.forward(100)
    t.right(360/n) # 외각 구하기
    
t.end_fill() # 색칠할 영역 끝

t.reset()
# 복잡한 도형 그리기
# 원
t.circle(100) # 반지름이 100인 원
# 반복해서 원 그리기
n = 60 # 반복 횟수
t.reset()
t.speed('fastest') # 속도는 가장 빠르게 설정
'''
거북이 속도 정하기
fastest : 0
fast : 10
normal : 6
slow : 3
slowest : 1
'''
for i in range(n):
    t.circle(120)
    t.right(360/n) # 오른쪽으로 6도 회전
    
# 선으로 복잡한 무늬 그리기
# t.reset()
# for i in range(300):
#     t.forward(i)
#     t.right(91)
    
# 연습문제 : 오각별 그리기
t. reset()
for i in range(5):
    t.fd(100)
    t.right(144)
    t.fd(100)
    t.left(72)
    
# 심사문제 : 별 그리기
t. reset()
n, length = map(int,input().split())

for i in range(n):
    t.fd(length)
    t.right((360/n) * 2)
    t.fd(length)
    t.left(360/n)


t.mainloop() # 터틀 창이 종료될 때까지 마우스, 키보드 입력 대기