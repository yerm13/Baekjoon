A, B = input().split()

A_reverse = int(A[2]+A[1]+A[0])
B_reverse = int(B[2]+B[1]+B[0])

if A_reverse > B_reverse :
    print(A_reverse)
else :
    print(B_reverse)
