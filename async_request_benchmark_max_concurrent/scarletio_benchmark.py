from scarletio import create_event_loop, WaitTillAll, Task
from scarletio.http_client import HTTPClient
from itertools import repeat

from timer import timer


URLS = [f'http://127.0.0.1:{port}/' for port in range(100, 105)]

async def request_task(url):
    async with session.get(url) as response:
        await response.read()


async def main_loop(count):
    tasks = []
    
    for x, url in zip(range(count), repeat(URLS)):
        for url in URLS:
            task = Task(request_task(url), LOOP)
            tasks.append(task)
    
    task = None
    
    await WaitTillAll(tasks, LOOP)
    
    for task in tasks:
        task.result()


async def main_task():
    # heat up
    await main_loop(2000)
    
    with timer():
        await main_loop(10000)


LOOP = create_event_loop()
session = HTTPClient(LOOP)
LOOP.run(main_task())
LOOP.stop()
