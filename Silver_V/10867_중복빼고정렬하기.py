# 시간초과 코드
n = int(input())
nums = input()
n_lst = [0 for i in range(2001)]

for i in range(n) :
    nn = int(nums.split()[i])
    n_lst[nn + 1000] += 1

for idx, n_cnt in enumerate(n_lst) :
    if n_cnt != 0 :
        print((idx - 1000), end = ' ')
        
        
####### 성공 코드 #######
# 중복 제거를 위해 set 사용
n = int(input())
n_lst = list(map(int, input().split()))

for i in sorted(list(set(n_lst))):
    print(i, end = ' ')
