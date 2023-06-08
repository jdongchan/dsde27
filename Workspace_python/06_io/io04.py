messages = ['리스트\n', '한번에\n', '넣어주고싶어요\n']

file = open('test01.txt', 'a', encoding = 'utf-8')
file.writelines(messages)
file.close()