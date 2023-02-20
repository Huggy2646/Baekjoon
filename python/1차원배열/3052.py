arr=list()
arr2=list()
arr3=list()
for i in range(10):
    a=int(input())
    a%=42
    arr.append(a)



while True:
    arr2.append(arr[0])
    arr3.append(arr.count(arr2[-1]))
    for i in range(arr.count(arr2[-1])):   # o(n^2)
        arr.remove(arr2[-1])
    if len(arr)==0:
        break

print(len(arr3))

'''
set_m=set()             #중복된 값들을 허용하지 않는 set(집합)구조를 이용하여 구현 O(n)
for i in range(10):
    a=int(input())
    set_m.add(a%42)
    
print(len(set_m))
'''