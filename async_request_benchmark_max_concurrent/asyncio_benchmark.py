from asyncio import wait, get_event_loop
from timer import timer
from aiohttp import ClientSession, TCPConnector
import warnings
import gc
from itertools import repeat


ClientSession.__del__ = lambda self: None


URLS = [f'http://127.0.0.1:{port}/' for port in range(100, 105)]

async def request_task(url):
    async with session.get(url) as response:
        await response.read()


async def main_loop(count):
    tasks = []
    
    for x, url in zip(range(count), repeat(URLS)):
        for url in URLS:
            task = LOOP.create_task(request_task(url))
            tasks.append(task)
    
    task = None
    
    await wait(tasks)
    
    for task in tasks:
        task.result()


async def main_task():
    # heat up
    await main_loop(2000)
    
    with timer():
        await main_loop(10000)


with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    
    LOOP = get_event_loop()
    session = ClientSession(loop=LOOP, connector=TCPConnector(limit=1000000, loop=LOOP))
    LOOP.run_until_complete(main_task())
    LOOP.close()
    session = None
    gc.collect()
    gc.collect()

