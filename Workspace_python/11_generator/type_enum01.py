from enum import Enum


class MyEnum(Enum):
    Python = 1
    MachineLearning = 2
    BigData = 3


print(MyEnum)
print(MyEnum.Python)
print(list(MyEnum.__iter__()))
