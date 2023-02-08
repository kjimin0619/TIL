from collections import deque

'''
기본적으로 후입선출(stack) LIFO
오른쪽 push = append <-> appendleft
오른쪽 pop = pop <-> popleft
'''

d = deque('ghi')
print(d.pop()) # i
print(d) # ['g', 'h']
d.appendleft('a')
d.append('k')
print(d) # deque(['a', 'g', 'h', 'k'])
