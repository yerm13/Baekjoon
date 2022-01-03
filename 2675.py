T = int(input())

for t in range(T) :
    R, S = input().split()
    P = ""
    for i in range(len(S)) :
        for j in range(int(R)) :
            P += S[i]
    print(P)
