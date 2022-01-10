test_case = int(input())
score = []

# list(map(함수, 리스트))
for i in range(test_case) :
    score.append(list(map(int, input().split())))

for List in score :
    n = List[0]
    del List[0]
    
    score_mean = sum(List) / n
    over = 0
    
    for sc in List :
        if sc > score_mean :
            over += 1   
    rate = (over / n) * 100
    
    print(f"{rate:.3f}%")
    
    
######## Numpy 사용 #######
import numpy as np

test_case = int(input())
score = []

for i in range(test_case) :
    score.append(list(map(int, input().split())))

for List in score :
    n = List[0]
    del List[0]
    
    score_mean = np.mean(List)
    over = 0
    
    for sc in List :
        if sc > score_mean :
            over += 1   
    rate = (over / n) * 100
    
    print(f"{rate:.3f}%")
