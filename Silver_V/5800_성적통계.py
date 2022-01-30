class_num = int(input())

for i in range(class_num) :
    score = list(map(int, input().split()))
    n = score[0]
    del score[0]
    
    max_score = max(score)
    min_score = min(score)
    
    dec_score = sorted(score, reverse = True)
    gap = []
    
    for j in range(n - 1) :
        gap.append(dec_score[j] - dec_score[j + 1])
    
    largest_gap = max(gap)
    
    print('Class', i + 1)
    print('Max {}, Min {}, Largest gap {}'.format(max_score, min_score, largest_gap))
