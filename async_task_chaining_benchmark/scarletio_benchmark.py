from scarletio import Future, create_event_loop, get_event_loop

from timer import timer


async def chain(loop, future, to_do):
    if to_do > 0:
        loop.create_task(chain(loop, future, to_do - 1))
    else:
        future.set_result(None)

    
async def main_loop():
    loop = get_event_loop()
    future = Future(loop = loop)
    
    loop.create_task(chain(loop, future, 400000))
    await future


async def main_task():
    # heat up
    await main_loop()
    
    with timer():
        await main_loop()


loop = create_event_loop()
loop.run(main_task())
loop.stop()
