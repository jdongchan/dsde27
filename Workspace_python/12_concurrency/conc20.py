import asyncio
from time import sleep

async def hello(name):
    print(f'hello, {name}')
    await asyncio.sleep(3) # 그냥 sleep(3)과 비교 - fast.api를 하는 경우 알고 있어야 한다.
    print(f'nice to meet you!')

async def main():
    await hello('coroutine')

    # coroutine -> task (awaitable)
    hello01 = asyncio.create_task(hello('async'))
    hello02 = asyncio.create_task(hello('await'))

    await hello01
    await hello02

if __name__ == '__main__':
    asyncio.run(main())