Running 10000 requests to 5 flask workers. With 10 task / worker for total of 50 tasks.

cpython3.8
```py
Starting scarletio benchmark
Task finished in 4.9868 seconds.
Starting asyncio + aiohttp benchmark
Task finished in 6.9030 seconds
```

Scarletio is 38% faster. That is pretty good not gonna lie.


pypy3
```py
Starting scarletio benchmark
Task finished in 3.1100 seconds.
Starting asyncio + aiohttp benchmark
Task finished in 5.9466 seconds.
```

91% faster ??
