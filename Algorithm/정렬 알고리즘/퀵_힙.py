## quick 정렬 & lamda 
'''
1. 정렬되지 않은 가장 맨 앞의 인덱스 선택(pivot)
2. 피벗보다 작은 요소(왼쪽), 큰 요소(오른쪽)로 분할
3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트 다시 정렬 (순환 호출 이용)
4. 위 과정을 리스트의 크기가 1이나 0이 될 때까지 반복
5. 정렬된 부분 배열들을 하나의 배열로 합병

추가 메모리 공간을 필요로 하지 않는다 - 공간 복잡도 O(log n)
시간 복잡도 최악의 경우 O(n^2)
'''
# lamda 매개변수 : 실행코드
# pred = boolean 
def quick_sort(lst,pred = lambda a,b : a<b): # default : 오름차순
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [v for v in lst[1:] if pred(v,pivot)]
    greater = [v for v in lst[1:] if not pred(v,pivot)]
    return quick_sort(less, pred) + [pivot] + quick_sort(greater, pred)


## 힙 정렬
'''
힙 구조를 사용하여 데이터 정렬
오름차순 정렬 - 최대 힙 max heap

시간 복잡도 O(nlog n)
'''
# 힙 생성 함수
def heapify(unsorted, index, heap_size):
    # 힙 성질 만족하는지 확인
    largest = index
    L = index*2 + 1 # 왼쪽 자식 노드
    R = index*2 + 2 # 오른쪽 자식 노드
    
    # 최댓값 연산
    if L < heap_size and unsorted[L] > unsorted[largest] :
        largest = L
    if R < heap_size and unsorted[R] > unsorted[largest] :
        largest = R
    
    # index가 최대값이 아니라면 교체 후 재귀 호출(반복)
    if index != largest :
        unsorted[index], unsorted[largest] = unsorted[largest], unsorted[index]
        heapify(unsorted, largest, heap_size)
        
def heap_sort(unsorted):
    print("before max heap : ", unsorted)
    n = len(unsorted)
    
    # 최대 힙 생성
    for i in range(n-1, -1, -1) : # 맨 아래(리프노드)부터 자리 탐색
        heapify(unsorted, i, n)    
    print("after max heap : ", unsorted )
    
    # 루트노드와 리프노드 교체 후 리프노드(구 루트노드) 고정 -> 다시 힙 생성
    for i in range(n-1,0, -1) :
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i) 
    return unsorted
    
if __name__ == '__main__':
    values = [19,50,7,85,32,1,23,41,11]
    print(quick_sort(values)) # 오름차순
    print(quick_sort(values, pred = lambda a,b : a > b)) # 내림차순
    print(quick_sort(values, pred = lambda a,b : abs(a) > abs(b))) # 절댓값

    names = ['nana','minji','soojung']
    print(quick_sort(names))
    print(quick_sort(names, pred=lambda a,b : len(a) < len(b))) # 문자열 길이 순서 정렬
    
    print("*"*30)
    print("after heap sort : ", heap_sort(values))
