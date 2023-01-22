from scarletio import Future, create_event_loop, get_event_loop

from timer import timer


def _set_timeout_if_pending(future):
    future.set_exception_if_pending(TimeoutError)


def _cancel_handle_callback(handle, future):
    handle.cancel()


async def main_loop_1(times, timeout):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop)
        future.apply_timeout(timeout)
        
        try:
            await future
        except TimeoutError:
            pass

async def main_loop_2(times):
    loop = get_event_loop()
    future = Future(loop = loop)
    future.set_result(None)
    
    for _ in range(times):
        future.apply_timeout(0.1)
        try:
            await future
        except TimeoutError:
            pass


async def main_loop_3(times):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop)
        loop.call_soon(future.set_result, None)
        future.apply_timeout(0.1)
        try:
            await future
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


loop = create_event_loop()
loop.run(main_task())
loop.stop()
