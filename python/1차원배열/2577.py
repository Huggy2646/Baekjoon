a=int(input())
b=int(input())
c=int(input())

count=0

arr=list(map(int,str(a*b*c)))
print(arr)

for i in range(10):
    for j in range(len(arr)):       #O(N^2)
        if arr[j]!=i:
            continue
        else:
            count+=1
    print(count)
    count=0


'''
a,b,c=int(input()),int(input()),int(input())
arr=str(a*b*c)

for i in range(10):
    print(arr.count(str(i)))    #list의 count함수를 이용하여 string형식으로 된 동일한 값의 갯수를 카운트하여 return O(N)

'''