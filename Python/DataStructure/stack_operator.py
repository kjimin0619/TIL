from stack_queue import *


# () 계산은 구현 x
def get_token_list(expr) :
    '''
    expr 문자열 입력받기
    연산자와 피연산자를 나누고, 이를 리스트에 담아서 리턴
    '''
    token_list = []
    operator = '-+*/^'
    operand = ''
    expr = expr.replace(" ", "") # 공백 제거
    
    for e in expr:
        if e in operator : 
            token_list.append(operand)
            token_list.append(e)
            operand = ''
        else :
            operand += e
            
    if operand != '' :
        token_list.append(operand)    

    return token_list

def inflix_to_postfix(token_list):
    opstack = Stack() # operator
    outcome = [] # outcome(postfix)
    operatorLevel = {'+': 0, '-': 0, '*' :1, '/':1}

    for token in token_list :
        # 연산자
        if token in '+-*/' :
            tokenLV = operatorLevel.get(token)   
            
            # stack에 연산자가 들어있는 경우
            if not(opstack.isEmpty()) :
                compLV = operatorLevel.get(opstack.top())   
                 
                while (compLV >= tokenLV):
                    outcome.append(opstack.pop())
                    if opstack.isEmpty() :
                        break
                    compLV = operatorLevel.get((opstack.top()))
                           
            opstack.push(token)
            
        # 피연산자    
        else : 
            outcome.append(token)
    
    # 남은 스택 정리
    while True:
        if (opstack.isEmpty()):
            return outcome
        else:
            outcome.append(opstack.pop())
   

def compute_postfix(token_list):
    OperandStack = Stack()
    
    for token in token_list :
        if token not in '+-*/' :
            OperandStack.push(int(token))
            
        else :
            a = OperandStack.pop()
            b = OperandStack.pop()
            
            if token == '+' : result = b + a
            elif token == '-' : result = b - a
            elif token == '*' : result = b * a
            elif token == '/' : result = b / a
            else : print("operator error...")
            
            OperandStack.push(result)
            
    return result


inflix = get_token_list('5 + 4 * 13 - 2')
postflix = inflix_to_postfix(inflix)
print("계산 결과 : ", compute_postfix(postflix))