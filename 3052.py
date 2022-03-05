a = []
result = []

for i in range(10) :           
    a.append(int(input()))     
    a[i] %= 42               

for j in a :                    
    if j not in result :       
        result.append(j)     

print(len(result))   
