nums = list(range(1,11))

print(nums)
print(dir(nums)) # iter가 있다.

nums_iter = nums.__iter__()
print(nums_iter)
print(type(nums_iter))

print(nums_iter.__next__()) # 다음 item을 리턴하는 함수
print(nums_iter.__next__())
print(nums_iter.__next__())

print(list(nums_iter))
print(list(nums_iter))

nums_iter = nums.__iter__()

for item in nums_iter:
    print(item, end=' ')




