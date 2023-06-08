import re

# regular expression (정규 표현식, 정규식)
'''
. : 문자 1개
^ : 문자열의 시작
$ : 문자열의 마지막
* : 0 or more
+ : 1 or more
? : 0 or 1
{n} : n번 반복
{n,m} : n번 부터 m번
{n,} : n번 부터 무한번
[] : 문자의 집합
| : OR
() : 괄호 안의 정규식 그룹

\w : [a-zA-Z0-9_] : a~Z, 0~9, _ 포함하는 모든 문자
\W : [^a-zA-Z0-9_] : 위의 문자 제외한 나머지 문자
\d : [0-9] : 0 부터 9
\D : [^0-9] : 숫자 제외한 나머지 문자
\s : [\t\n\r\f\v] : 공백문자
\S : [^\t\n\r\f\v] : 공백 제외한 모든 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[숫자] : 지정된 숫자만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝
'''

txt = 'This module provides regular expression matching operations similar to those found in Perl.'

match_txt = re.match(r'[a-zA-Z]*', txt) # 맨처음 대문자,소문자 알파벳 0~ 연결되어 있는 문자열 하나만 찾아옴.
print(match_txt)

# [ ] : 문자 집합
# * : 0 ~ more
# a-z : 소문자 알파벳
# A-Z : 대문자 알파벳
# -> 소문자나, 대문자 알파벳 집합이 0개 ~ more

search_txt = re.search(r'[\w]+', txt)
print(search_txt)

print(match_txt.group(0))
print(search_txt.group(0))

findall_txt = re.findall(r'[a-zA-Z]*', txt)
findall_txt = re.findall(r'[a-zA-Z]+', txt)
print(findall_txt)
# *을 사용하면 공백도 포함, +을 사용하면 공백은 없다. 공백은 문자열임.

find_t_txt = re.findall(r't[a-zA-Z]*', txt)
print(find_t_txt)

# r로 시작하여 r로 끝나는 문자열을 출력해 주세요!
find_rr_txt = re.findall(r'r[a-zA-Z]*r', txt)
print(find_rr_txt)

# o로 시작해서 s로 끝나는
find_os_txt = re.findall(r'o[a-zA-z]+s', txt)
print(find_os_txt)

find_os_txt2 = re.findall(r'[\w]*o[\w]*s[\w]*', txt)
print(find_os_txt2)

address = '''
010-1111-1234
010-1234-5678
010-3456-7890
'''

phone_list = address.split('\n')
print(phone_list)

phone_list = list(filter(None, phone_list))
print(phone_list)

phone_middle = list(map(lambda x: x.replace(re.search(r'\-[\d]*\-', x).group(0),'-****-'), phone_list))
print(phone_middle)