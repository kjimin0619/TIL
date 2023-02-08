'''
31. 재귀호출

파이썬에서는 최대 재귀 깊이를 1,000으로 정해둠
'''

# 재귀 호출에 종료 조건 만들기
def hello(cnt):
    if cnt == 0 :
        return
    print('hello world! ', cnt)
    cnt -= 1
    hello(cnt)
    
hello(10)
print()

# 재귀 호출로 팩토리얼 구하기
def factorial(n):
    if n == 1 :
        return 1
    return n*factorial(n-1)

print(factorial(8))

# 회문 판별
def is_palindrome(word):
    if len(word) < 2 : return True
    if word[0] != word[-1] : return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))
## TODO : 왜 None type 객체가 출력되는가?

# 피보나치 수
def fib(n):
    if n == 0 :
        return 0
    elif n == 1 or n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)
  
print(fib(10))
