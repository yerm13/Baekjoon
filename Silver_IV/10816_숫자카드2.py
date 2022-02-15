N=int(input())
num=list(map(int,input().split()))
m=int(input())
num1=list(map(int,input().split()))
new_dic={}
for i in num:
    if i in new_dic:
        new_dic[i]+=1
    else:
        new_dic[i]=1
for i in num1:
    if i in new_dic:
        print(new_dic[i],end=" ")
    else:
        print(0,end=" ")
