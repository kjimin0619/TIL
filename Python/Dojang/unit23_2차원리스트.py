'''
23. 2차원 리스트

2차원 리스트 : 가로 x 세로
* 가로크기2, 세로크기3 행렬 제작
리스트 = [[값,값],[값,값],[값,값]]
-> [값,값]
   [깂,값]
   [값,값]

* 2차원 리스트 요소 접근
세로인덱스 : 행
가로인덱스 : 열
리스트[세로인덱스][가로인덱스]
a = [[10, 20], [30, 40], [50, 60]]
a[2][1] => 60

* 톱니형 리스트 
파이썬에서는 가로 크기가 불규칙한 톱니형(jagged list) 제작 가능
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
     
* 2차원 튜플
튜플 안에 튜플, 튜플 안에 리스트, 리스트 안에 튜플 가능

* 알아보기 쉽게 출려가기
사각형 구조를 유지하여 출력하기 : pprint 모듈의 pprint 함수 사용
'''

# 구조 유지한 채 출력하기
# indent : 들여쓰기 칸 수, width : 가로 폭
from cmath import sqrt
from pprint import pprint
a = [[10, 20], [30, 40], [50, 60]]
pprint(a, indent=4,width=20)

# 반복문으로 2차원 리스트 요소 모두 출력하기
print('\n반복문으로 2차원 리스트 출력')
for x,y in a:
    print(x,y)
    
print('반복문 두 번 사용하기')
for i in a :
    print()
    for j in i:
        print(j, end='-')
        
print('\nfor와 range 사용하기')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    
print('\nwhile 반복문 한 번 사용하기')
i = 0 # len(a) = 3
while i<len(a) :
    x,y = a[i]
    print(x,y)
    i += 19
    
print('\nwhile 반복문 두 번 사용하기')
i = 0
while i<len(a) :
    j = 0
    while j<len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i +=1
    
# 반복문으로 리스트 만들기
print('\n1차원 리스트')
a = []
a = [i for i in range(10)]
print(a)
a = [0] * 9
print(a)


print('\n2차원 리스트')
b = []
for i in range(3):
    line = [0] * 2
    b.append(line)
print(b)

print('\n리스트 표현식으로 2차원 리스트 만들기')
a = [[0]*2 for i in range(3)]
print(a)    

# 톱니형 리스트 만들기
print('\n톱니형 2차원 리스트')
a = [3,1,3,2,5] # 가로 크기를 저장한 리스트
b = [] # 빈 리스트
for i in a:
    line = [0]*i
    b.append(line)
print(b)
# list comprehension
k = [[0]*i for i in a]
print(k)

# 2차원 리스트 정렬
# sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)
print('sorting--')
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
# index 1 기준으로 정렬
print(sorted(students, key = lambda student : student[1]))
# index 2 기준으로 정렬
sorted_student = sorted(students, key = lambda student : student[2], reverse = True)
print(sorted_student)

# 리스트의 할당과 복사
# 2차원 이상의 다차원 리스트를 완전히 깊은 복사하려면,
# copy.deepcopy 함수 사용해야 함.
import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][0] = 'h'
print(b)
print(a)

# 연습문제
print('\n3차원 리스트 만들기')
# 높이2, 세로크기4, 가로크기3
a = [[[0]*3 for i in range(4)] for j in range(2)]
print(a)
# 다른 방법
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)
# 리스트[높이인덱스][세로인덱스][가로인덱스]