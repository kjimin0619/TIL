class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,val):
        self.items.append(val)
        
    def pop(self):
        try :
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
            
    def top(self):
        try :
            return self.items[-1]
        except IndexError :
            print("Stack is empty")
            
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
class Queue :
    def __init__(self):
        self.__items = []
        self.__front_index = 0
        self.__length = 0
        
    def enqueue(self, val):
        self.__items.append(val)
        self.__length = self.__length + 1
        
    def dequeue(self):
        if self.__front_index == len(self.__items):
            print("Queue is empty")
            return None
        
        else :
            x = self.__items[self.__front_index]
            self.__front_index += 1
            self.__length = self.__length - 1
            
            return x
        
    def isEmpty(self):
        return (self.__length == 0)
        
    def front(self):
        return self.__items[0]
    
    def len(self):
        return self.__length