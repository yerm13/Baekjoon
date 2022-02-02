n = int(input())
fac = 1
lst = []

for i in range(1, n+1) :
    fac = fac * i

len_str = len(str(fac))
for i in range(len_str) :
    lst.append(str(fac)[i])

lst.reverse()
for i in range(len_str) :
    if lst[i] != '0' :
        print(i)
        break
