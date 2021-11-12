from asyncio import wait_for, get_event_loop
from timer import timer, LOOP_COUNT

async def dummy_task():
    pass

async def main_loop():
    count = 0
    while True:
        await wait_for(dummy_task(), timeout=0.1)
        
        count += 1
        if count > LOOP_COUNT:
            break

async def main_task():
    # heat up
    await main_loop()
    
    with timer():
        await main_loop()

loop = get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(main_task())
loop.close()
