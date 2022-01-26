import sys
t_case = int(input())
n_lst = []

for _ in range(t_case) :
    n_lst.append(int(sys.stdin.readline()))

for i in sorted(n_lst):
    sys.stdout.write('{}\n'.format(i))
