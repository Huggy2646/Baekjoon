# s=input()
# for i in range(97,123):
#     _=chr(i)
#     if _ in s:
#         print(s.index(_),end=" ")
#     else:
#         print("-1",end=" ")
#         continue


print(*map(input().find,map(chr,range(97,123))))
"""
map을 이용하면 좋음
print(i for i in list(map(input().find,map(chr,range(97,123)))), end="")
or
print(*map(input().find,map(chr,range(97,123))))) --> 이때 *이 뭐임???? 대체??? 검색해도 안나와;;;

(A)
아무도 답을 안주시네요.

저도 대략적으로 알다가 다시 찾아본 내용을 설명드릴께요.

pyhton 에는 packing, unpacking 이라는 것이 있는데, unpacking 에 관련된 문법입니다.

a = 1

b = 2

일떄, 

c = a,b

라고 하면

(1,2) 가 c 에 튜플로 들어가는 것이 packing 이고 (두 변수를 하나에 묶어 넣는)

d,e = c 

라고 하면 d, e에 각각 1, 2 가 들어가는 것이 unpacking 입니다. (한 변수의 있는 것을 분리해서 변수에 넣는 것..)

이것의 사용처는 

a,b = b,c 와 같이 swap 으로 쓸 수도 있고..

함수에서

def func(a,b):

  return a+b

라는 것이 있으면

func(c)라고 쓸수 없습니다, (c == (1,2) 일때)

저렇게 부르려고 하면 a 에 (1,2)를 넣고 b를 찾으려고 하는데 값을 안준 것으로 생각힙니다.

원래의 의도대로 a=1, b=2 로 넣으려면 unpacking 을 해야하고

func(*c)로 부르면 됩니다.

print 문은 아시다시피 print(a,b,c)식으로 부르면 각각 변수 값을 공백으로 구분해서 출력합니다.

위 예에서 pint(c)와 print(*c)의 차이는

(1,2) 와 같이 튜블로 묶여서 보이느냐 1 2 와 같이 내용만 공백 구분해서 출력되냐의 차이가 되겠네요.



따라서, print(*map(input().find,map(chr,range(97,123)))) 하면

안쪽의 map 은 소문자 리스트를 만들꺼고

바깥 map 이 입력에서 소문자의 인덱스들을 찾을 것이고 이것이 packing 되어 있을텐데

print 문에 *으로 unpacking 해서 넣어주면 공백으로 구분해서 출력해줍니다.
"""