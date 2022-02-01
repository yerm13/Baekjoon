t = int(input())
cnt = 0
num = list(map(int, input().split()))

for i in num :
    lst = []
    for j in range(1, i) :
        if i % j == 0 :
            lst.append(j)
    if len(lst) == 1 :
        cnt += 1

print(cnt)
