# 선택 정렬
'''
1. 정렬되지 않은 가장 맨 앞의 인덱스 선택
2. 현재 인덱스+1 부터 끝까지 가장 작은 값을 찾아서 현재 인덱스와 바꿈(swap)
3. 과정 반복

하나의 배열에서 값을 바꿈- 공간 복잡도 O(1)
시간 복잡도 O(n^2)
'''
def selection_sort(lst):
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)) : 
            if lst[min_idx] > lst[j] :
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i] # swap
    return lst
    
# 버블 정렬
'''
현재 원소와 다음 원소를 비교하여 조건에 맞으면 교환
뒤에서부터 앞으로 정렬해나가는 구조

하나의 배열에서 값을 바꿈 - 공간 복잡도 O(1)
시간 복잡도 O(n^2)
'''
def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1) :
        for j in range(i) :
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
    return lst
    
# 삽입 정렬
'''
두 번째 원소부터 시작
앞의 원소들과 비교하여 삽입할 위치를 지정
이때, 삽입할 위치 왼편의 원소들은 이미 정렬 끝난 상태
본인보다 작은 원소를 만날 때까지 왼쪽 원소와 swap 

하나의 배열에서 값을 바꿈 - 공간 복잡도 O(1)
시간복잡도 O(n^2)
'''
def insertion_sort(lst): 
    for end in range(1, len(lst)) :
        for i in range(end, 0, -1) :
            if lst[i-1] > lst[i] :
                lst[i-1], lst[i] = lst[i], lst[i-1]
            else :
                break
    return lst
            
# 병합  정렬
'''
1. divide(분할) : n개의 원소를 갖는 배열을 n/2개의 원소를 갖는 작은 배열 2개로 나눔
2. conquer(정복) : 각각의 작은 배열들을 정렬
3. combine(병합) : 정렬된 작은 배열들을 병합

n개의 원소를 n/2개씩 나눈다 - 공간 복잡도 O(n)
시간 복잡도 O(nlog n)
'''
def merge_sort(lst) :
    # 크기가 1이면 반환
    if len(lst) <= 1 :
        return lst
    
    # 입력 리스트 2분할
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    # 2분할된 리스트 각각 merge sort 진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)    
    return merge(left_, right_)

def merge(left, right) :
    # 길이가 1로 쪼개진 리스트를 순서대로 병합하여 정렬 리스트에 저장
    i, j = 0 , 0
    sorted_list = []
    
    while i < len(left) and j < len(right) :
        if left[i] < right[i] :
            sorted_list.append(left[i])
            i += 1
        else :
            sorted_list.append(right[j])
            j += 1
    
    while i < len(left) :
        sorted_list.append(left[i])
        i += 1
        
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

if __name__ == "__main__" :
    print("정렬 알고리즘 - 선택, 버블, 삽입, 병합")
    
    # 정렬 결과 확인하기
    lst = [25,10,12,20,55,36]
    print(selection_sort(lst))
    print(bubble_sort(lst))
    print(insertion_sort(lst))
    print(merge_sort(lst))

    # [10, 12, 20, 25, 36, 55]