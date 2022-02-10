Comparing task speed between asyncio and scarletio.

Using pypy3
```py
Starting asyncio benchmark
Task finished in 1.3668 seconds.
Starting scarletio benchmark
Task finished in 1.1031 seconds.
```
Scarletio is 24% faster than asyncio. Pypy showing off.


Using python3.8
```py
Starting asyncio benchmark
Task finished in 3.9313 seconds.
Starting scarletio benchmark
Task finished in 3.9119 seconds.
```
Almost same time! Asyncio's C futures and tasks really punch a lot.


Using python3.5
```py
Starting asyncio benchmark
Task finished in 7.2931 seconds.
```
Scarletio is 86% faster! In python3.5 asyncio is not yet using C for speedups. It really shows, oh no. There might be
a few other internal changes as well.


The result shows that meanwhile scarletio unexpectedly can go head to head with C speedups, it requires you to be more
specific, increasing code length.
