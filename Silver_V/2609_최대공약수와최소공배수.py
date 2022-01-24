n1, n2 = map(int, input().split())
g_list = []

for i in range(1, 10001) :
    if n1 % i == 0 and n2 % i == 0 :
        g_list.append(i)
G = max(g_list)
L = int((n1 * n2) / G)

print(G)
print(L)
