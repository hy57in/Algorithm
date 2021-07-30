t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    a = (n-1)%h+1
    b = (n-1)/h+1
    print(int(a*100+b))