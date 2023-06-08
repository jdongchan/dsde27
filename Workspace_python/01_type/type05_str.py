# str : text sequence 즉, 순서가 존재한다.

# single quotation mark ' ' = 문자열 처리
a = 'hello, world!'
print(a)

# hello, 'python'!  ' ' 안에 ' ' 를 쓰기 위해서는 escape 문자를 사용하면 된다.
b = 'hello, \'python\'!'
print(b)
# escape sequence (escape character)

# single quotation mark ''' ''' = 여러 줄 주석 / 여러 줄 문자열
c = '''hello
python
    abc
        def!
'''
print(c)

# double quotation mark " " = 문자열 처리
d = "hello, world!"
print(d)

# double quotation mark """ """ = 여러 줄 주석/ 여러 줄 문자열
e = """hello
python
    abc
        def
"""
print(e)

# hello, "python"! " " 안에 " " 을 사용하기 위해서 escape 문자 \ 를 사용.
f = "hello, \"python\"!"
# single 안에 double 혹은 double 안에 single 을 사용하면 escape 문자 필요 없음.
f_1 = 'hello, "python"!'
print(f)
print(f_1)
# hello, 'python'!
g = "hello, 'python'!"
print(g)

print("hello, \npython!") # \n 은 줄바꿈
i = 'c:\test' # \t는 tab
print(i)

# raw string
j = r'c:\test' # raw string r'' 을 사용하면 \문자를 그대로 사용할 수 있다.
print(j)

# 더하면 옆에 붙고 문자열을 곱하면 두번 출력된다. 대신 sep이 없어서 hellohellopython!
print('hello' * 2 + "python!")