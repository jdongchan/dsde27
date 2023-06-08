import os # 사무 자동화할 때 많이 사용한다.

# print(os.environ)
print(dict(os.environ).keys())
print(os.environ.get('USER')) # WINDOWS는 USERNAME
print(os.environ.get('PYTHONPATH')) # 현재 사용하고 있는 PYTHON 경로

print(os.getcwd()) # 현재 디렉토리

print(os.listdir()) # 현재 디렉토리에 있는 파일들

# 디렉토리 만들어주는 기능
if not os.path.exists('test'):
     os.mkdir('test')
     print('make directory!')
else:
     print('already exists!')

# 디렉토리의 이름을 바꾸는 기능
# os.rename('./test', 'test2')

os.rmdir('test2')