# This file is a modified version of the benchmark found at:
# https://bugs.python.org/issue32204

from asyncio import get_event_loop, iscoroutine, gather

from timer import timer

class Batch:
    batches = {}

    @classmethod
    def schedule(cls, key):
        if not Batch.batches:
            loop.call_later(0, Batch.schedule_batches)

        future = loop.create_future()
        Batch.batches.setdefault(cls, []).append((key, future))

        return future

    @staticmethod
    def schedule_batches():
        for batch in list(Batch.batches.keys()):
            loop.create_task(Batch.resolve_batch(batch, Batch.batches.pop(batch)))

    @staticmethod
    async def resolve_batch(batch, futures):
        batch_keys = [key for key, future in futures]

        future_results = batch.resolve_futures(batch_keys)
        if iscoroutine(future_results):
            future_results = await future_results

        for key_future_pair, result in zip(futures, future_results):
            key, future = key_future_pair
            future.set_result(result)

    @staticmethod
    def resolve_futures(batch):
        raise NotImplemented()

    @classmethod
    async def gen(cls, key):
        return await cls.schedule(key)

    @classmethod
    async def genv(cls, keys):
        return await gather(*[cls.gen(key) for key in keys])


class DoubleBatch(Batch):
    @staticmethod
    def resolve_futures(batch):
        return [x+x for x in batch]


class SquareBatch(Batch):
    @staticmethod
    def resolve_futures(batch):
        return [x*x for x in batch]


async def double_square(x):
    double = await DoubleBatch.gen(x)
    square = await SquareBatch.gen(double)
    return square


async def square_double(x):
    square = await SquareBatch.gen(x)
    double = await DoubleBatch.gen(square)
    return double


async def triple_double(x):
    d1 = await DoubleBatch.gen(x)
    d2 = await DoubleBatch.gen(d1)
    d3 = await DoubleBatch.gen(d2)
    return d3


async def double_square_square_double(x):
    ds = await double_square(x)
    sd = await square_double(ds)
    return sd


async def big_batch(x):
    return await gather(
        gather(
            square_double(x + 0),
            square_double(x + 1),
            square_double(x + 2),
        ),
        gather(
            double_square(x * 1),
            double_square(x * 2),
            double_square(x * 3),
        ),
        DoubleBatch.genv(range(x, x + 5, +1)),
        SquareBatch.genv(range(x, x - 5, -1)),
        gather(
            triple_double(x - 1),
            triple_double(x - 2),
            triple_double(x - 3),
        ),
        gather(
            double_square_square_double(x * 5),
            double_square_square_double(x * 7),
            double_square_square_double(x * 9),
        ),
    )


async def main_loop():
    return await gather(*[
        big_batch(x) for x in range(0, 5000)
    ])


async def main_task():
    # heat up
    await main_loop()
    
    with timer():
        await main_loop()

loop = get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(main_task())
loop.close()
