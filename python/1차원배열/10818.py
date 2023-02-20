def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
        
            
    low=0 #작은수 구하기
    low=arr[0]
    for i in arr:
        if low >=i:
            low=i

    high=0 #큰수 구하기
    high=arr[0]
    for i in arr:
        if high <= i:
            high=i

    print(low,end=" ")
    print(high)

    return 0
    
main()