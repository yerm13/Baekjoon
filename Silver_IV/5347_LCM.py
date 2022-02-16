t = int(input())

for _ in range(t) :
    a, b = map(int, input().split())
    lst = []
    for i in range(1, 1000001) :
        if a % i == 0 and b % i == 0 :
            lst.append(i)
    G = max(lst)
    L = int((a * b) / G)
    print(L)
