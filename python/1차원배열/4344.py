for i in range(int(input())):
    arr=list(map(int,input().split()))
    avr=sum(arr[1:])/len(arr[1:])
    avr_up=list(filter(lambda x:x>avr,arr[1:]))
    print("{:.3f}".format(len(avr_up)/len(arr[1:])*100)+"%")

'''
result_arr=list()
for i in range(int(input())):
    arr=list(map(int,input().split()))
    avr=sum(arr[1:])/len(arr[1:])

    avr_up=list(filter(lambda x:x>avr,arr[1:]))

    result=("{:.3f}".format(len(avr_up)/len(arr[1:])*100))
    result_arr.append(result)

for i in range(len(result_arr)):
    print(result_arr[i]+"%")
'''


'''

for i in range(int(input())):
    arr=list(map(int,input().split()))
    avr_up=list(filter(lambda x:x>sum(arr[1:])/len(arr[1:]),arr[1:]))
    print("{:.3f}".format(len(avr_up)/len(arr[1:])*100)+"%")
'''


