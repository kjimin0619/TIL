'''
16. for & range

range의 증가폭을 음수로 지정할 수 있음
for i in range(10,0,-1)

숫자의 순서를 반대로 뒤집을 수 있음
for 변수 in reversed(range(횟수))

** reversed()
: 반대방향으로 순회하는 iterator 반환
'''

# 순서 뒤집기
for i in reversed(range(10)):
    print('hello',i)
    
# 문자열 뒤집기
# 파이썬에서 문자열 뒤집는 방법?
for i in reversed('python'):
    print(i,end='')
    
print()
print()

# 문자열 뒤집어서 새 변수 객체에 넣기
# 1. slice
letter = 'Jimini'
reversed_letter = letter[::-1]

print('original : {0} \nreversed : {1}'.format(letter, reversed_letter))

# 2. reversed(), join() 활용
# join : 매개변수로 들어온 리스트에 있는 요소를 합쳐서 하나의 문자열로 반환
letter = 'Jimini'
reversed_letter = "".join(reversed(letter))

print('original : {0} \nreversed : {1}'.format(letter, reversed_letter))

# join 활용
a = ['abcd','mylove','forever']
print(a)

result1 = "".join(a)
result2 = "~".join(a)

print('result1 : {0}, result2 : {1}'.format(result1, result2))
# 3. for loop
letter = 'Jimini'
reversed_letter = ''
for i in letter:
    reversed_letter = i + reversed_letter
    
print('original : {0} \nreversed : {1}'.format(letter, reversed_letter))





# # 연습문제
# X = [10,20,30,40]

# for i in X :
#     print(i*10, end=' ')

# # 심사문제
# print('\n')
# dan = int(input())
# for i in range(1,10):
#     print('{0} * {1} = {2}'.format(dan,i,dan*i))