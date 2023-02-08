# quick sort ver.python
# lamda 매개변수 : 실행코드
# pred = boolean 
def quick_sort(lst,pred=lambda a,b : a<b): # default : ascending 
    if not lst:
        return lst
    pivot = lst[0]
    less = [v for v in lst[1:] if pred(v,pivot)]
    greater = [v for v in lst[1:] if not pred(v,pivot)]
    return quick_sort(less, pred) + [pivot] + quick_sort(greater, pred)


if __name__ =='__main__':
    values = [5,-4,2,0,10,-7,9]
    print(quick_sort(values)) # ascending
    print(quick_sort(values, pred = lambda a,b : a > b)) # descending
    print(quick_sort(values, pred=lambda a,b : abs(a) > abs(b)))

    names = ['nana','minji','soojung']
    print(quick_sort(names))
    print(quick_sort(names, pred=lambda a,b : len(a) < len(b)))

