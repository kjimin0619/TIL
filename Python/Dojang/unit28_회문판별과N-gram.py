'''
28. 회문 판별과 N-gram 만들기
'''

## 회문 판별
# 회문(palindrome) : 거꾸로 읽어도 앞으로 읽어도 똑같은 단어와 문장! 우영우~
# s = input('회문 판별할 문자열을 입력하세요 : ')
s = 'hello'
is_palindrome = True
repeat = len(s) // 2
for i in range(repeat):
    if s[i] != s[-1-i] :
        is_palindrome = False
        break

print('for문 탐색 결과 : ', is_palindrome)

# 문자열 뒤집기 활용
print('시퀀스 뒤집기 결과 :', s==s[::-1])

# 리스트와 reversed 사용
print('리스트와 reversed 사용 결과 :', list(s) == list(reversed(s))) 

# join 메서드와 reversed 사용
print('join 메서드 & reversed 사용 결과 : ', s == ''.join(reversed(s)))


## N-gram 만들기
print('\n<N-gram 만들기>\n')
# n-gram : 문자열에서 n개의 연속된 요소를 추출하는 방법
text = 'hello'
# 글자 단위 2-gram
for i in range(len(text) -1):
    print(text[i:i+2], end=' ') # he el ll lo
print()

# 단어 단위 2-gram
text = 'this is python script'
words = text.split()
for i in range(len(words)-1):
    print(words[i],words[i+1])
    
    
# zip 함수로 2-gram 만들기
print('\nzip함수 활용')
text = 'hello'
two_gram = zip(text,text[1:])
for i in two_gram:
    print(i[0],i[1],sep='')
    

text = 'this is python script'
two_gram = text.split()
two_gram = zip(two_gram, two_gram[1:])
for i in two_gram:
    print(i)
# print(two_gram) # zip object

# 리스트표현식으로 N-gram 만들기
print()
text = 'hello'
three_gram = [text[i:i+3] for i in range(3)]
print('리스트표현식 :',three_gram) # n=3. 리스트표현식만 사용

# zip 활용
temp = [text[i:] for i in range(3)] # n = 3
print(temp)
# zip에 넣기
temp = list(zip(*temp)) # 리스트 안의 요소르 콤마로 구분해서 넣어주려면 리스트 앞에 * 붙이기
print('리스트표현식 & zip 활용 :', temp)
# 리스트 언패킹 : 리스트에 *를 붙이는 방법 (이후 30unit에서 설명)

# 연습문제
n = int(input())
text = input().split()

if len(text) < n :
    print('wrong')
else :
    n_gram = zip(*[text[i:] for i in range(n)])
    for i in n_gram :
        print(i)

# 심사문제 : words.txt 파일에서 회문 찾기
with open('words.txt','r') as file :
    lines = file.readlines()
    for word in lines :
        word = word.strip('\n')
        # 회문 판단
        if word == word[::-1] :
            print(word)