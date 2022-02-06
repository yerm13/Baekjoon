# 2217 : 로프

n = int(input())
rope = []
result = [] 

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True) # 내림차순 정렬

for i in range(n):
    result.append(rope[i] * (i + 1)) # n번째 큰 수에 n 곱해주기

print(max(result))
