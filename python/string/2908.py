s=list(input().split())
for i in range(len(s)):
    s[i]=int("".join(reversed(s[i])))
if s[0]<s[1]:
    print(s[1])
else:
    print(s[0])



'''
max함수로 젤 큰수 파악 가능하고
input()[::-1].split()이 가능하다
'''