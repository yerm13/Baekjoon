import sys
t_case = int(input())
n_lst = [0 for i in range(10000)]

for i in range(t_case) :
    num = int(sys.stdin.readline())
    n_lst[num - 1] += 1

for idx, n_cnt in enumerate(n_lst) :
    if n_cnt != 0 :
        for i in range(n_cnt) :
            sys.stdout.write('{}\n'.format(idx + 1))
