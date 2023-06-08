# 해석하는 숙제
# 1
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
print('-----')
# str.join(iterable)
# Return a string which is the concatenation of the strings in iterable.
# iterable한 문자열의 결합
# A TypeError will be raised if there are any non-string values in iterable, including bytes objects.
# The separator between elements is the string providing this method.

# [''.join(['*' for i in range(i + 1)]) for i in range(5)]
# i = 0    i = 1     i = 2         ...  i = 4
# ['*']   ['*""*']   ['*""*""*']       ['*""*""*""*""*']
# '\n'.join['*',

# '\n'.join(['*','**','***','****','*****'])
# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print('-----')
# '\n'.join(['','','',''].join( '****','***','**','*'])

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print('-----')
# '\n'.join(['    *','   **', '  ***', ' ****', '*****'])

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print('-----')
# '\n'.join(['*****',' ****', '  ***', '   **', '    *'])

# 5
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
print('-----')
# '\n'.join(['    *','   ***','  *****',' *******','*********'])