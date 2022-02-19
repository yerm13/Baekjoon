import sys
t = int(sys.stdin.readline())

for i in range(t) :
    n = int(sys.stdin.readline())
    cnt = 0
    i = 5
    
    while i <= n:
        cnt += n // i
        i *= 5
    print(cnt)
