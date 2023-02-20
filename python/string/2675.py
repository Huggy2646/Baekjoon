for i in range(int(input())):
    r,s = input().split()
    print("".join(map(lambda x:x*int(r),s)))