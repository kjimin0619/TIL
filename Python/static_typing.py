from typing import List
# 파이썬에서 정적 타입 선언하기
# 참고 블로그 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=passion053&logNo=221070020739

# 함수 입출력 타입 정의
# 변수명 : type
def double(thing : int) -> int :
    return thing + thing

# 함수 입출력 타입 선언 X
def times5(thing) :
    return thing * 5

if __name__ == "__main__" :
    print(double(2))
    # print(double("2")) # error. double 함수의 입력 데이터 타입은 무조건 정수
    # print(double([1,2])) # error

    print(times5(2))
    print(times5("2"))
    print(times5([1,2]))
