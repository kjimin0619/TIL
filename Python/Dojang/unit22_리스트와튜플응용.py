'''
22. 리스트와 튜플 응용

<리스트 조작 메서드>
append : 요소 하나 추가
extend : 리스트를 연결하여 확장
insert : 특정 인덱스에 요소 "추가"
pop : 요소를 삭제한 뒤 삭제한 요소 반환
remove(value) : 리스트에서 특정 값 찾아서 삭제
index(value) : 리스트에서 특정 값의 인덱스 구하기
count(value) : 특정 값의 갯수 구하기
reverse() : 뒤집기
sort() : 정렬
    sort() : 오름차순. sort(reverse=False)
    sort(reverse = True) : 내림차순
    
    * sorted(list) 내장햠수
    sort() 메서드는 정렬 결과를 리스트에 바로 반영
    sorted(리스트변수) 함수는 새 리스트 반환
clear() : 모든 요소 삭제

* 리스트가 비어있는지 확인하기
: if list # 요소가 있으면 True
-> 리스트가 비어있는 경우 인덱스를 -1로 지정하면 에러 발생


<리스트로 스택과 큐 만들기>
- 스택(후입선출)
일반적인 리스트를  왼쪽으로 90도 돌리면 스택임
pop()과 append() 그냥 해도 됨

- 큐(선입선출)
pop(0)을 사용해야 큐
파이썬에서는 collection 모듈의 deque를 제공
덱 : 양쪽 끝에서 추가/삭제 가능한 자료구조
append() : 오른쪽에 요소 추가
appendleft() : 왼쪽에 요소 추가
pop() : 오른쪽 요소 삭제
popleft() : 왼쪽 요소 삭제

<리스트의 할당과 복샤>
b = a 처럼 리스트를 다른 변수에 할당하면 하나의 리스트를 가리키는 두 개의 별명이 생기는 것
즉, a is b ==  True

a,b를 완전히 다른 두 객체로 만들기 : copy()
a is b == False

<반복문으로 리스트의 요소를 모두 출력하기>
인덱스와 요소 함께 출력 : for 인덱스, 요소 in enumerate(리스트)
=========================================
<튜플>
index(값) : 특정 값의 인덱스
count(값) : 특정 값의 개수
튜플 표현식 : tuple(식 for 변수 in 리스트 if 조건식)
map 사용 가능
min, max, sum 사용 가능

'''
# append
a = [1,2,3,4,5]
a.append(43)
a.append(['a','b','c'])
print(a) # [1,2,3,4,5,43,['a','b','c']]
print(len(a)) # 7

# extend
a.extend(['아','뇽','하','세','요'])
print(a)

# insert(index,value)
a.insert(0,'메롱')
print(a)
# cf) 특정 인덱스 요소 변경 
a[0] = 'dkd'
print(a) # ['dkd', 1, 2, 3, 4, 5, 43, ['a', 'b', 'c'], '아', '뇽', '하', '세', '요']


# slice 활용
# 시작과 끝 인덱스를 같게 지정하면 해당 인덱스의 요소를 덮어쓰지 않으면서 요소 여러개 추가 가능
b = [13,2,56,2,6,230]
b[1:1] = [555,444,444,2222]
print(b) # [13, 555, 444, 444, 2222, 2, 56, 2, 6, 230]

# pop(index) == del list[index]
b.pop() # last index
print(b)

b.pop(1)
print(b)

# remove
# 같은 값이 여러 개 있을 경우, 처음 찾은 값만 삭제
b.remove(444)
print(b)

# index(value)
print(b.index(13))

# enumerate
for i, v in enumerate(b):
    print(i,v)
    
# enumerate 시작 인덱스 설정 버전
for i, v in enumerate(b, start = 1):
    print(i, v)
    
# for 반복문에서 인덱스로 요소 출력하기
list1 = [1,2,3,4,5,6,7]
for i in range(len(list1)):
    print(list1[i])
    
# while 반복문으로 요소 출력
i = 0
while i<len(list1):
    print(list1[i])
    i += 1
    
# 리스트에서 가장 작은 수와 가장 큰 수 구하기
print('search biggest, smallest')
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest : smallest = i
print(smallest)
# sort method
print('what if using \'sort\' method?')
a.sort()
print(a,a[0])
# min, max 내장 함수
print('min, max 내장 함수 이용')
print(min(a))

# 리스트 요소 합계 구하기 : sum 내장 함수
print(sum(a))

# 리스트 표현식
# 식 for 변수 in 리스트
# list(식 for 변수 in 리스트)
sample1 = [i for i in range(10)] # 이렇게 만드는 게 더 성능이 좋음
print("sample1 :", sample1)
sample2 = list(i+6 for i in range(5))
print("sample2 :", sample2)
sample3 = [i for i in range(10) if i % 2 != 0]
print("sample3 :", sample3)
sample4 = [i*j for i in range(8) 
           for j in range(3)]
print("sample4(len) : ", sample4, len(sample4))

# list에 map 사용하기
# map에는 리스트 뿐만 아니라 모든 반복가능한 객체를 넣을 수 있음
# map은 원본 리스트를 변경하지 않고 새 리스트 반환
a = [1.2, 4.23, 66.4]
# b = list(map(int,a))
b,c,d = map(int,a)
e = map(int,a)
print(b,c,d) # 1,4,66
print(e, type(e)) # <map object at 주소> <class 'map'>

# input().split() & map
print('input.split 에 map 적용')
input, s = map(int,input().split())
print(input)


# 퀴즈
a = [1,2,3]
a[len(a):] =  [40]
a.append([80,40,50])
a[1:3] = ['a','b'] # [1, 'a', 'b', 40, [80, 40, 50]]
a[1:1] = ['asdffsdafdsfds','asdfafds']
print(a) # [1, 'asdffsdafdsfds','asdfafds','a', 'b', 40, [80, 40, 50]]

# 연습문제
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 심사문제
start, end = map(int,input().split())
print(start, end)
lis = [2**i for i in range(start, end+1) if not (i == start + 1 or i == end-1)]
print(lis)