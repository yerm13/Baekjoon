lst = []
n = input()

for i in range(len(n)) :
    lst.append(n[i])
    
sort_lst = sorted(lst, reverse = True)

for i in range(len(n)) :
    print(sort_lst[i], end = '')
