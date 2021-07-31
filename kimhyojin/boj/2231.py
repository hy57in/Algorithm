n = int(input())

answer = 1000000
for i in range(1, n+1):
    tmp = sum(map(int, str(i)))
    tmp += i

    if tmp == n:
        answer = min(i, answer)
        print(answer)
        break
    if i == n:
        print(0)