num = input()
cnt = 0

while len(num) > 1 :
    num = str(sum(map(int, list(num))))
    cnt += 1
    
print(cnt)
print("YES" if int(num)%3 == 0 else "NO")
