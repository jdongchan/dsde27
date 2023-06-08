# iterable : 반복 가능한 (값을 순서대로 꺼내올 수 있는)
# iterator : 반복 (값을 순서대로 꺼내는) 객체
# lazy evaluation : 실행될 때 연산
# __iter__()


nums = list(range(1, 11))
print(f'nums : {nums}')
print(f'dir(nums) : {dir(nums)}')

nums_iter = nums.__iter__()
print(f'nums_iter : {nums_iter}')
print(f'type(nums_iter) : {type(nums_iter)}')

print(nums_iter.__next__())
print(nums_iter.__next__())
print(nums_iter.__next__())


print(list(nums_iter))

# print(nums_iter.__next__())
print(list(nums_iter))

nums_iter = nums.__iter__()

for item in nums_iter:
    print(item, end=' ')











