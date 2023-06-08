import asyncio
from time import sleep

async def hello(name):
    print(f'Hello, {name}')
    await asyncio.sleep(3)
    print('nice to meet you')

async def main():
    await hello('coroutine')\

    hello01 = asyncio.create_task(hello('async'))
    hello02 = asyncio.create_task(hello('await'))

    await hello01
    await hello02

if __name__ == '__main__':
    # 비동기 실행 asyncio.run - 고수준 실행. 사람이 사용하고 이해하기 편하다.
    # asyncio.run(main())

    # 저수준 실행 - conc20이랑 똑같이 실행된다. 컴퓨터에 가깝다.사람이 사용하기 불편하지만 여러가지 어려운 작업을 수행.
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()