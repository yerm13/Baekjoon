t = int(input())

for i in range(t) :
    lst = []
    a, b = map(int, input().split())
    for j in range(1, 45001) :
        if a % j == 0 and b % j == 0 :
            lst.append(j)
    G = max(lst)
    L = int((a * b) / G)
    print(L)
