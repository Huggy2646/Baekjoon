def noself(n):
    if n<10:
        m=n+n
        return m
    elif 10<=n<100:
        m=n+(n//10)+(n%10)
        return(m)
    elif 100<n<1000:
        m=n+(n//100)+(n%100//10)+(n%10)
        return m
    else:
        m=n+(n//1000)+(n%1000//100)+(n%100//10)+(n%10)
        return m

a=list()
b=list(range(10000))

for i in range(10000):
    a.append(int(noself(i)))

# try:
#     for k in range(1,10001):
#         if int(k) not in n:
#             print(k)
# except TypeError:
#     pass

try:
    for i in set(a):
        b.remove(i)
except ValueError:
    pass

for i in range(len(b)):
    print(b[i])


'''
이거 숏코딩 할 때 string을 생각하자 멍청아 대가리 멍청해가지곤 시발
'''