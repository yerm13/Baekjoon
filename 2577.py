A = int(input())
B = int(input())
C = int(input())
ABC = str(A*B*C)

c0 = 0 ; c1 = 0 ; c2 = 0 ; c3 = 0 ; c4 = 0
c5 = 0 ; c6 = 0 ; c7 = 0 ; c8 = 0 ; c9 = 0

for i in range(len(ABC)) :
    if ABC[i] == '0' :
        c0 += 1
    elif ABC[i] == '1' :
        c1 += 1
    elif ABC[i] == '2' :
        c2 += 1
    elif ABC[i] == '3' :
        c3 += 1
    elif ABC[i] == '4' :
        c4 += 1
    elif ABC[i] == '5' :
        c5 += 1
    elif ABC[i] == '6' :
        c6 += 1
    elif ABC[i] == '7' :
        c7 += 1
    elif ABC[i] == '8' :
        c8 += 1
    else :
        c9 += 1
        
print(c0) ; print(c1) ; print(c2) ; print(c3) ; print(c4)
print(c5) ; print(c6) ; print(c7) ; print(c8) ; print(c9)
