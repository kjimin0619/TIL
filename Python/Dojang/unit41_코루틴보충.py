import time

def coroutine_test():
    text = (yield)
    print('while 시작합니다.')
    while True:
        print("text = ",end=""), print(text)
        text = yield ('wonderful ' + text + '\n')


if __name__ == "__main__":
    cr = coroutine_test()
    print("cr=",end=""), print(cr)

    next(cr)
    time.sleep(5)

    print("send 1")
    print(cr.send("morning"))
    time.sleep(5)

    print("send 2")
    print(cr.send("afternoon"))
    time.sleep(5)

    print("send 3") 
    print(cr.send("evening"))
    time.sleep(5)