from hata import KOKORO, Task, future_or_timeout
from timer import timer, LOOP_COUNT

async def dummy_task():
    pass

async def main_loop():
    count = 0
    
    while True:
        task = Task(dummy_task(), KOKORO)
        future_or_timeout(task, 0.1)
        await task
        
        count += 1
        if count > LOOP_COUNT:
            break

async def main_task():
    # heat up
    await main_loop()
    
    with timer():
        await main_loop()

KOKORO.run(main_task())
KOKORO.stop()
