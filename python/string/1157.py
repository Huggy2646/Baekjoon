# alpa="".join(map(chr,range(64,91)))
# arr= list(map(alpa.find,input().upper()))
# max,value=0,0

# for i in set(arr):
#     if max<arr.count(i):
#         max=arr.count(i)
#         value=i
#     elif max==arr.count(i):
#         print("?")
#         value=False
#         break
#     else:
#         continue

# if value!=False:
#     print(alpa[value])

arr=input().upper()
for i in map(chr,range(64,91)):
    arr.count(i)