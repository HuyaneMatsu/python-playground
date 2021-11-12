Benchmark for using looped task timeouts with different technologies mainly targeting hata's new repeat timeout
feature.

Cpython3.8
```py
Starting dummy
Task finished in 0.0070 seconds.
Starting asyncio basic
Task finished in 1.7431 seconds.
Starting hata basic
Task finished in 0.9388 seconds.
Starting hata repeat timeout
Task finished in 0.0208 seconds.
```

pypy3.6
```py
Starting dummy
Task finished in 0.0001 seconds.
Starting asyncio basic
Task finished in 0.4350 seconds.
Starting hata basic
Task finished in 0.2420 seconds.
Starting hata repeat timeout
Task finished in 0.0062 seconds.
```

The results show, that `repeat_timeout` is indeed a super lightweight looped timeouter, as it is able to beat asyncio
80 times consistently.

Note, that this is an extremely edge case scenario, but I like it.
