import asyncio

async def hello(future, name):
    print(f'hello, {name}')
    await asyncio.sleep(3)
    future.set_result('nice to meet you')

async def main():
    # 비동기 시작
    loop = asyncio.get_event_loop()

    future01 = loop.create_future()
    future02 = loop.create_future()

    loop.create_task(hello(future01, 'async'))
    loop.create_task(hello(future02, 'await'))

    print(await future01)
    print(await future02)
    # awaitable : 비동기적으로 동작할 수 있다. -> coroutine, future, task

if __name__ == '__main__':
    asyncio.run(main())