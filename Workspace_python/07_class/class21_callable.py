class Hello:
    # 객체를 함수처럼 사용! -> callable object
    def __call__(self, name):
        print(f'hello, {name}')

if __name__ == '__main__':
    greetings = Hello()
    greetings('dongchan')
    # callable object
    # Hello()('dongchan')