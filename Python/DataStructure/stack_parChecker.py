from stack_queue import *
S = Stack()
S.push(10)
S.push(2)
print(S.top()) # 2
print(S.isEmpty()) # False

# 스택 예시 : 괄호 맞추기
def parChecker(parseq):
    S = Stack()
    for p in parseq :
        if p == '(' :
            S.push(p)
        elif p == ')' :
            if S.isEmpty() :
                return False
            else :
                S.pop()
        
    if S.isEmpty :
        return True
    else :
        return False

print(parChecker('(()()())')) # true

# 중괄호, 대괄호 섞인 문장
def mixParCheck(parseq):
    parDict = {')':'(', 
               '}':'{', 
               ']':'['}
    S = Stack()
    for p in parseq:
        if p in '({[' :
            S.push(p)
        else :
            if S.isEmpty() :
                return False
            elif S.top() == parDict.get(p) : # p = },],)
                S.pop()
            else :
                return False
    if S.isEmpty() :
        return True
    else :
        return False
    
print(mixParCheck('{}[]()')) # true
print(mixParCheck('{[()]}')) # true
print(mixParCheck('{[()')) # false 
                