# set : 순서 x, 중복 X

# 실행할 때 마다 출력 순서 변경됨
a = {'1','5','2','3','3','3','4'}
print(a)

# 숫자를 hashing 시 숫자 값이 주소 값으로 정의됨 -> 숫자가 자동 오름차순 정렬됨.
b = {1,5,2,3,3,3,4}
print(b)
f = {5,4,5,6,7,2,1}
print(f)
print('-------')
# set() 생성자
c = set([1,2,3,4,5])
print(c)
c = set((1,2,3,4,5))
print(c)

a.add('6')
print(a)
print(a.pop())
print(a.pop())
print(a.pop())
print(a)
print('------')
# d = set(["h","e","l","l","o",...])
d = set("hello, world!")
print(d)

# 집합
left = {"a","b","c","d"}
right = {"c","d","e","f"}

# 합집합 union
print(left.union(right))
print(left | right)

# 교집합 intersection
print(left.intersection(right))
print(left & right)

# 차집합 difference
print(left.difference(right))
print(left - right)

# frozen set
e = frozenset([1,2,3,4,5])
print(e)
print(type(e))
print(dir(set))
print(dir(frozenset))

# frozen set은 합,교,차와 같은 연산만 하고 값을 추가 불가능
# e.add(6)












