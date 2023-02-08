# node
class Node :
    def __init__(self, key = None, value = None):
        self.key = key # key
        self.next = None # link
        self.value = value 
        
    def __str__(self):
        return str(self.key)
    
# 연결리스트
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
            
    def __str__(self):
        return "->".join(str(v) for v in self)
    
    def __len__(self):
        return self.size
    
    # 지원연산 구현
    # 1. 삽입
    def pushFront(self, key, value=None):
        new_node = Node(key,value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0 :
            self.head = new_node
        
        else :
            v = self.head
            while v != None : # tail 노드 찾기 시작
                v = v.next
            v.next = new_node
        self.size += 1
        
    # 2. 제거
    def popFront(self) :
        if self.size == 0 :
            return None
        
        x = self.head
        key = x.key
        self.head = x.next
        
        del x
        self.size -= 1
        return key
        
    def popBack(self):
        if self.size == 0 : # 빈 리스트
            return None
        
        pre,tail = None, self.head
        while tail.head != None :
            pre = tail
            tail = tail.next
        
        if self.size == 1 : # 크기가 1인 리스트 
            self.head = None
            
        else : # 크기가 2 이상인 리스트
            pre.next = None # tail.next와 동일
        
        key = tail.key    
        del tail
        self.size -= 1
        return key
    
    # 3. 특정 노드 탐색 ; 제너레이터 활용   
    def search(self, key) :
        for n in self :
            if n.key == key :
                return n
        # 찾고자 하는 노드가 없는 경우  
        return None    
    
    # 4. 특정 노드(v) 제거
    def remove(self,v) :
        # 빈 리스트
        if (v == None or self.size == 0) :
            pass
        
        # v가  head 노드인 경우
        elif self.head == v :
            self.popFront()
        
        # 그 외 경우
        else :
            present_node = self.head
            prev_node = None
            
            while present_node != None:
                prev_node = present_node
                present_node = present_node.next
                
                if present_node == v :
                    prev_node.next = present_node.next
                    del present_node
                    self.size = self.size - 1
                    
if __name__ == '__main__' :
    print("메인 실행")