from stack_queue import *
def Josephus(n,k):
    Q = Queue()
    
    # 큐 안에 숫자 전부 enqueue
    for v in range(1,n+1):
        Q.enqueue(v)
    
    # start game
    while Q.len() > 1 :
        for _ in range(1,k):
            Q.enqueue(Q.dequeue())
        Q.dequeue()
        
    print("The end..")
    
    return Q.dequeue() # len(Q) == 1

print("Survive..!", Josephus(6,2))
