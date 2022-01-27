m = int(input())
n = int(input())
lst = []
 
for i in range(m, n+1):
    cnt = 0
    for j in range(1, i+1):             
        if i % j == 0:
            cnt += 1                 
            if cnt > 2:
                break
    if cnt == 2:
        lst.append(i)
if len(lst) != 0:
    print(sum(lst))
    print(lst[0])
else:
    print('-1')
