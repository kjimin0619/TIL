# 값 비교시 is, is not 사용하지 말 것
# 값 비교는 ==. != 으로만
# 2개 이상의 조건문 : 하나라도 참이면 t -> or, 모두 참이여야 t -> and
a = {n for n in range(30) if n%3==0 or n%5==0}
print(a)

b = [n for n in range(30) if n%3==0 or n%5==0]
print(b)

# 유닛26 세트 퀴즈
c = [i for i in range(10) if i !=2 and i != 7]
print(c)

x = {'a':1,'b':2, 'delta' :1, 'd' : 30}

a = {key:value for key,value in x.items() if value != 30 and key != 'delta'}
print(a)

for i in range(1,31):
    if i != 1 and i != 30 : print(i,end=' ')