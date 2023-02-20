def main():
    arr1=dict()
    arr2=dict()
    count=0
    high=0

    for i in range(9):
        key=int(input())
        arr1[i]=key
        arr2[key]=i
        if i == 0:
            high=arr1[0]
        elif i>=1 and high<arr1[i]:
            high=arr1[i]
        else:
            continue      
        

    print(high)
    print(arr2[high]+1)
    return 0

main()        