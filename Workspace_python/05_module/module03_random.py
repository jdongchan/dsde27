import random

# random.random : 0.0 <= x < 1.0 무작위의 값을 하나 만들어준다.
random_num = random.random()
print(random_num)

# random.randint(a, b) : a <= x <= b 무작위의 정수 값을 하나 만들어준다.
# 일반적으로는 <= , < 가 많다.
random_int = random.randint(1,100)
print(random_int)
