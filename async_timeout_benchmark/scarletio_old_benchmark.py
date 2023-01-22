from scarletio import Future, create_event_loop, get_event_loop

from timer import timer


class _TimeoutHandleCanceller:
    __slots__ = ('_handle',)
    
    def __init__(self):
        self._handle = None
    
    def __call__(self, future):
        handle = self._handle
        if handle is None:
            return
        
        handle.cancel()
        self._handle = None
        future.set_exception_if_pending(TimeoutError())
    
    def cancel(self):
        handle = self._handle
        if handle is None:
            return
         
        self._handle = None
        handle.cancel()



def future_or_timeout(future, timeout):
    loop = future._loop
    callback = _TimeoutHandleCanceller()
    handle = loop.call_later(timeout, callback, future)
    if handle is None:
        raise RuntimeError(
            f'`future_or_timeout` was called on future with a stopped loop; loop = {loop!r}.'
        )
    
    callback._handle = handle
    future.add_done_callback(callback)


async def main_loop_1(times, timeout):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop)
        future_or_timeout(future, timeout)
        
        try:
            await future
        except TimeoutError:
            pass


async def main_loop_2(times):
    loop = get_event_loop()
    future = Future(loop = loop)
    future.set_result(None)
    
    for _ in range(times):
        future_or_timeout(future, 0.1)
        try:
            await future
        except TimeoutError:
            pass


async def main_loop_3(times):
    loop = get_event_loop()
    
    for _ in range(times):
        future = Future(loop)
        loop.call_soon(future.set_result, None)
        future_or_timeout(future, 0.1)
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
