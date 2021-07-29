a = int(input())

for x in range(a):
    cnt = 0
    h, w, n = map(int, input().split())
    for i in range(w):
        for j in range(h):
            cnt = cnt + 1
            YY = str(j+1)
            if i < 10:
                XX = '0' + str(i+1)
            else:
                XX = str(i+1)
            answer = YY + XX
            if cnt == n:
                print(answer)
