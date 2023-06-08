# c에서 standard input output 이라 함.

file = open('test01.txt','w') # open은 파일 열어주세요. 'w' - 쓰기 모드
file.write('Hello, World!\n')
file.close() # open을 사용하면 close 반드시 사용해야 한다.

'''
r : 읽기 - read
w : 쓰기 (기존 내용 덮어쓰기) - write
a : 쓰기 (기존 내용 이어서 쓰기) - append
x : 쓰기 (새로운 파일 만들어서 쓰기)
t : text
b : binary
'''