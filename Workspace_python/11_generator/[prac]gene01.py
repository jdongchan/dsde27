def my_generator(end):
    i = 0
    while i < end:
        i += 1

        yield i ** 2

# generator : A function which returns a generator iterator. It looks like a normal function except that
# it contains yield expressions for producing a series of values usable in a for-loop or that
# can be retrieved one at a time with the next() function.

# generator iterator : Each yield temporarily suspends processing, remembering the location execution state
# (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

if __name__ == "__main__":
    nums = my_generator(10)
    print(nums)

    print(nums.__next__()) # 첫번째
    print(nums.__next__()) # 두번째
    print(nums.__next__()) # 세번째
    print(next(nums)) # 네번째

    for item in nums: # 다섯번째부터 끝까지
        print(item)

# The yield expression is used when defining a generator function or
# an asynchronous generator function and thus can only be used in the body of a function definition.
# Using a yield expression in a function’s body causes that function to be a generator function,
# and using it in an async def function’s body causes that coroutine function to be an asynchronous generator function.