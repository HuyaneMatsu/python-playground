from hata import KOKORO, repeat_timeout
from timer import timer, LOOP_COUNT

async def dummy_task():
    pass

async def main_loop():
    count = 0
    
    for _ in repeat_timeout(0.1):
        await dummy_task()
        
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