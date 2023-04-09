import asyncio

async def something(num):
    print('A:'+num)
    await asyncio.sleep(2)
    print('B:'+num)

something('10')