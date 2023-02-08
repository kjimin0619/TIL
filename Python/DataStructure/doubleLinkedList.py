class Node :
    def __init__(self, key=None):
        self.key = key
        self.next = self.prev = self
    def __str__(self) :
        return str(self.key)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None()
        self.size = 0
        
    def __iter__(self):
        v = self.head
        while v != None :
            yield v
            v = v.next
    
    def __str__(self):
        return "->".join(str(v) for v in self)
    
    def __len__(self):
        return self.size
    
    def splice(self, a, b, x):
        if a == None or b == None or x == None :
            return

        ap = a.prev
        bn = b.next
        
        ap.next = bn
        bn.prev = ap
        
        x.next = a
        a.prev = x
        
        xn = x.next
        b.next = xn
        xn.prev = b
    
if __name__ == "__main__":
    print("메인 실행")