n=int(input())
arr=[0]*n
sum=0 #결과
m=0


for i in range(n):
    arr[i]=input()

for i in range(n):
    for j in arr[i]:
        if j=="O":
            m+=1
            sum+=m
        else:
            m=0
    print(sum)
    m=0
    sum=0