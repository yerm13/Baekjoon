n = int(input())
score = map(int, input().split())
score_list = list(score)
max_score = max(score_list)
new_list = []
for each in score_list:
    new_list.append(each/max_score*100)
avr = sum(new_list)/len(new_list)
print("%.2f"%avr)
