from asyncio import wait, get_event_loop
from timer import timer
from aiohttp import ClientSession
import warnings
import gc


ClientSession.__del__ = lambda self: None

class TARGET_COUNTER:
    COUNT = 0


URLS = [f'http://127.0.0.1:{port}/' for port in range(100, 105)]

async def request_task(url):
    while True:
        count = TARGET_COUNTER.COUNT - 1
        TARGET_COUNTER.COUNT = count
        if count <= 0:
            break
        
        async with session.get(url) as response:
            await response.read()


async def main_loop():
    tasks = []
    
    for x in range(10):
        for url in URLS:
            task = LOOP.create_task(request_task(url))
            tasks.append(task)
    
    task = None
    
    await wait(tasks)
    
    for task in tasks:
        task.result()


async def main_task():
    # heat up
    TARGET_COUNTER.COUNT = 2000
    await main_loop()
    
    with timer():
        TARGET_COUNTER.COUNT = 10000
        await main_loop()

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    
    LOOP = get_event_loop()
    session = ClientSession(loop=LOOP)
    LOOP.run_until_complete(main_task())
    LOOP.close()
    session = None
    gc.collect()
    gc.collect()

