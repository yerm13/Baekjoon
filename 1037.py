count = int(input())
aliquot = []
aliquot_input = input().split()

for i in range(count) :
    ali = int(aliquot_input[i])
    aliquot.append(ali)
    
aliquot.sort()
N = aliquot[0] * aliquot[count - 1]
print(N)
