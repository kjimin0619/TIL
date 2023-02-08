base = 2
def square(n):
    return base ** n

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def greeting(self):
        print('안녕하세요 저는 {}입니다.'.format(self.name))
        
        
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(add(10,20))