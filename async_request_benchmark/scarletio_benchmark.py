from scarletio import create_event_loop, WaitTillAll, Task
from scarletio.http_client import HTTPClient

from timer import timer

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
            task = Task(request_task(url), LOOP)
            tasks.append(task)
    
    task = None
    
    await WaitTillAll(tasks, LOOP)
    
    for task in tasks:
        task.result()


async def main_task():
    # heat up
    TARGET_COUNTER.COUNT = 2000
    await main_loop()
    
    with timer():
        TARGET_COUNTER.COUNT = 10000
        await main_loop()


LOOP = create_event_loop()
session = HTTPClient(LOOP)
LOOP.run(main_task())
LOOP.stop()
