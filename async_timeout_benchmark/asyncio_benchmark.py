from asyncio import Future, TimeoutError, get_event_loop, wait_for

from timer import timer


async def main_loop_1(times, timeout):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop = loop)
        
        try:
            await wait_for(future, timeout)
        except TimeoutError:
            pass

async def main_loop_2(times):
    loop = get_event_loop()
    future = Future(loop = loop)
    future.set_result(None)
    
    for _ in range(times):
        try:
            await wait_for(future, 0.1)
        except TimeoutError:
            pass


async def main_loop_3(times):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop = loop)
        loop.call_soon(future.set_result, None)
        try:
            await wait_for(future, 0.1)
        except TimeoutError:
            pass


async def main_task():
    # heat up
    await main_loop_1(2000, 0.0)
    await main_loop_1(2000, 0.0001)
    await main_loop_2(2000)
    await main_loop_3(2000)
    
    with timer():
        await main_loop_1(100000, 0.0)
    
    with timer():
        await main_loop_1(10000, 0.0001)

    with timer():
        await main_loop_2(100000)
    
    with timer():
        await main_loop_3(100000)


loop = get_event_loop()
loop.run_until_complete(main_task())
loop.close()
