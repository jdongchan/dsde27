from enum import Enum


subjects = Enum("MyEnum", ["Python", "MachineLearing", "BigData"])

print(subjects)
print(subjects.Python)
print(list(subjects.__iter__()))
