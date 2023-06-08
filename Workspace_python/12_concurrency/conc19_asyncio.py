import asyncio # asynchronous : 동시에 일어나지 않는 (비동기적인)

async def hello(name):
    print(f'hello, {name}')
    await asyncio.sleep(3)
    print('nice to meet you!')

if __name__ == '__main__':
    # 지금은 동기적으로 실행되고 있음
    asyncio.run(hello('gildong'))
    asyncio.run(hello('sunshin'))