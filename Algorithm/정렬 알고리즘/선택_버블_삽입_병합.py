# 정렬 알고리즘(오름차순) - 선택, 버블, 삽입, 병합

## 선택 정렬 
# 1. 정렬되지 않은 가장 맨 앞의 인덱스 선택
# 2. 현재 인덱스 +1 부터 끝까지 가장 작은 값을 찾아서 현재 인덱스와 바꿈(swap)
# 3. 과정 반복
# 하나의 배열에서 값을 바꿈- 공간복잡도  O(1)
# 시간복잡도 O(n^2)
def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)) : 
            if lst[min_idx] > lst[j] :
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i] # swap
    return lst
    
## 버블 정렬
# 현재 원소와 다음 원소를 비교하여 조건에 맞으면 교환
# 뒤에서부터 앞으로 정렬해나가는 구조
# 하나의 배열에서 값을 바꿈 - 공간 복잡도 O(1)
# 시간복잡도 O(n^2)
def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1) :
        for j in range(i) :
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
## 삽입 정렬
# 두 번째 원소부터 시작
# 앞의 원소들과 비교하여 삽입할 위치를 지정
# 이때, 삽입할 위치 왼편의 원소들은 이미 정렬 끝난 상태
# 본인보다 작은 원소를 만날 때까지 왼쪽 원소와 swap 
# 하나의 배열에서 값을 바꿈 - 공간 복잡도 O(1)
# 시간복잡도 O(n^2)
# 선택 정렬이나 버블 정렬에 비해 상대적으로 빠르다
def insertion_sort(lst): 
    for end in range(1, len(lst)) :
        for i in range(end, 0, -1) :
            if lst[i-1] > lst[i] :
                lst[i-1], lst[i] = lst[i], lst[i-1]
            else :
                break
            
## 병합  정렬
def merge_sort(lst) :
    pass

if __name__ == "__main__" :
    print("sdf")
