def string(arr):
    return list(map(str,arr))

def number(arr):
    return list(map(int,arr))

def diff(arr):
    n=0
    count=0
    arr=number(arr)
    n=arr[1]-arr[0]
    for i in range(0,len(arr)-1):
        if n==arr[i+1]-arr[i]:
            count+=1
        else:
            continue
    if len(arr)-1==count:
        return True
    else:
        return False
        

def han(arr):
    count=0
    if(len(arr)<100):
        count=len(arr)

    elif(len(arr)>=100):
        arr2=arr[99:len(arr)+1]
        for i in arr2:
            if diff(i)==True:
                count+=1
        count+=99
    print(count)

arr=list(map(str,range(1,int(input())+1)))
han(arr)
'''
야이 무식한 새끼야
한수들을 봐라
a=111 or 123 or 136 ---> a[0]+a[-1]//2==[len(a)//2]
1234, 12345 ---> a[0]+a[-1]//2==[len(a)//2]

등차수열에서 a,b,c가 있으면 b=(a+c)/2이다.
'''