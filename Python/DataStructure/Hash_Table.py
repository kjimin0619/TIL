import sys

h,m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

m = m + t
if (m >= 60) :
    h = h + (m//60)
    m = m % 60

print(h,m)