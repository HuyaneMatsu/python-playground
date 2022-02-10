from scarletio import repeat_timeout, create_event_loop
from timer import timer, LOOP_COUNT

async def dummy_task():
    pass

async def main_loop():
    count = 0
    
    with repeat_timeout(0.1) as loop:
        for _ in loop:
            await dummy_task()
            
            count += 1
            if count > LOOP_COUNT:
                break


async def main_task():
    # heat up
    await main_loop()
    
    with timer():
        await main_loop()

loop = create_event_loop()
loop.run(main_task())
loop.stop()
