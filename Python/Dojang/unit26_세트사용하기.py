'''
26. 세트(집합) 사용하기

'''

### 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)
# set는 요소의 순서가 정해져 있지 않음. 따라서 출력마다 요소 순서가 달라짐
# 요소가 중복될 수는 없음(집합이기 때문)
# []로 특정 요소 출력 불가능

# 세트에 특정값 있는지 확인하기
print('orange' in fruits) # true

# set를 사용하여 세트 만들기
# set(반복가능한 객체)
# 1. 문자열 넣으면?
a = set('apple')
print(a) # {'l', 'p', 'a', 'e'} 이렇게 분해됨
# 2. range를 넣으면?
a = set(range(4))
print(a)
# 3. 아무것도 지정하지 않으면 빈 세트
a = set()
print(a) # set()
# cf) 세트 안에 세트를 넣을 수는 없음

# frozenset(반복가능한객체) : 내용을 변경할 수 없는 세트
# 프로즌세트 안에는 세트를 넣을 수 있음. 단, 프로즌 세트만 넣을 수 있음
a = frozenset(range(10))
print('frozen set :',a)

### 집합 연산 사용하기
a = {1,2,3,4,5}
b = {4,5,6,7}
# 1. 합집합 : |,union
print('합집합 : ', a|b, set.union(a,b))
# 2. 교집합 : &,intersection
print('교집합 :',a&b, set.intersection(a,b))
# 3. 차집합 : -,difference
print('차집합 :',a-b,set.difference(a,b))
# 4. 대칭차집합 : ^,symmetric_difference
print('대칭차집합 :',a^b, set.symmetric_difference(a,b))

# 집합 연산 후 할당 연산자 사용
# a |= b == a.update(b)
# a &= b == a.intersection_update(b)
# a -= b == a.difference_update(b)
# a ^= b == a.symmetric_difference_update(b)
a = {1,2,3,4}
b = {5}
a.update(b)
print(a)

# 부분집합, 상위 집합 확인
# 세트1이 세트2의 부분집합인지 확인 : 세트1 <= 세트2, 세트1.issubset(세트2)
# 진부분집합 확인 : <
a = {1,2,3}
b = {1,2,3,4,5}
print(a<=b) # true
print(a.issubset(b)) # true

# 세트1이 세트2의 상위집합인지 확인 : 세트1 >= 세트2, 세트1.issuperset(세트2)
# 진상위집합 : >
a = {1,2,3,4,5,6}
b = {1,2,3}
print(a.issuperset(b)) # true
print(a >= b) # tue

# 세트가 같은지 다른지 확인 : ==
# 세트가 겹치치 않는지 확인 : isdisjoint(안 겹치면 true)
a = {1,2,3,4}
b = {5,6}
print(a.isdisjoint(b)) # true

### 세트 조작
# 추가 : add(요소)
# 삭제(없으면 에러) : remove(요소)
# 삭제하고 없으면 그냥 넘어가기 : discard(요소)
# 임의 요소 삭제 후 반환(없으면 에러) : pop()
# 모든 요소 삭제 : clear()
# 요소 개수 구하기 : len(세트)

### 할당과 복사
# = 할당
# copy() 복사 -> 서로 다른 객체로 만들어짐

### 반복문으로 모든 요소 출력
a = {1,2,3,4,5,6,7,89,899}
for i in a :
    print(i)
    # 세트 요소에는 순서가 없으므로 출력 시 순서는 매번 달라짐
    
### 세트 표현식
# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)
a = {i for i in 'dasdgeees'} # 중복문자는 바로 삭제함
print(a)

# if 조건문 사용
a = {i for i in 'pineapple' if i not in 'apl'}
print(a) 

# 연습문제 : 공배수
a = {i for i in range(1,101) if i % 3 == 0}
b = {i for i in range(1,101) if i % 5 == 0}
print(a&b)

# 심사문제 : 공약수
num1, num2 = map(int, input().split())
# num1,2의 공약수 구하기
a = {i for i in range(1,num1+1) if num1%i==0}
b = {i for i in range(1,num2+1) if num2%i==0}
divisor = a&b
result = 0
if type(divisor) == set :
    result = sum(divisor)
print(result)