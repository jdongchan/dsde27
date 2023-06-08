name = "dongchan"
age = 100

# print(name + age)
print(name + str(age))
print(name, age)
print(name, age, sep="    ")
print(name, age, end="!")
print('a')
# default가 \n를 !으로 바꾸었기 때문에 줄바꿈이 없어짐.
print('name', name, sep=":", end="\t")
# 구분자에 : 가 들어가고 마지막에 tab이 들어감. 줄이 안바뀜
# 그리고 두 번째 구분자 : 마지막에 default \n. 줄 바꿈
print('age', age, sep=":")
print("a")

# % values
print('% values')
print('name : %s' % name)
print('name : %s \t age : %d' %(name, age))

# str.format()
print('str.format()')
print('name : {0} \t age : {1}'.format(name, age))
# f-string
print('f-string')
print(f'name : {name} \t age : {age}')





