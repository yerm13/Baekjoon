'''
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
이 수들이 A안에 존재하는지 알아내면 된다.

M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

n = int(input())
n_lst = set(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))
lst = [0 for i in range(m)]

for i in range(m) :
    if m_lst[i] in n_lst :
        lst[i] += 1

for i in range(m) :
    print(lst[i], end = '\n')
