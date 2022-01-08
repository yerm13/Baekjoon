apt = [[0 for col in range(14)] for row in range(15)]

for i in range(15) :
    apt[i][0] = 1
for j in range(14) :
    apt[0][j] = j+1
for k in range(1, 15) :
    for l in range(1, 14) :
        apt[k][l] = apt[k][l - 1] + apt[k - 1][l]
        
T = int(input())

for t in range(T) :
    k = int(input())
    n = int(input())
    print(apt[k][n - 1])
