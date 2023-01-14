Comparing task chaining speed between asyncio and scarletio. (Maybe task chaining is a bad word for this.)

Task chaining means that each task starts a new one as: task `n` starts task `n + 1`.
The last scheduled task marks the loop as done.

Task chaining is popular at event driven programming where on event a new task is started for each related event
handler.

Using pypy3
```py
Starting asyncio benchmark
Task finished in 1.4320 seconds.
Starting scarletio benchmark
Task finished in 0.3888 seconds.
```
Scarletio takes only 27% of the time.


Using python3.8
```py
Starting asyncio benchmark
Task finished in 2.9027 seconds.
Starting scarletio benchmark
Task finished in 1.3800 seconds.
```
Scarletio takes 48% of the time.


Using python3.11
```py
Starting asyncio benchmark
Task finished in 1.9743 seconds.
Starting scarletio benchmark
Task finished in 0.8588 seconds.
```
Scarletio takes 44% of the time.


The results might be weird, "How can scarletio beat C code in Cpython?". The recipe has two steps:
- C asyncio tasks are actually not much faster than scarletio tasks.
- This benchmark is actually event loop heavy.

So what are the differences in the event loops?
- Scarletio expects that tasks are short running and they are created after io operations, so there is no more io
  needed and we can prefer the chained tasks over polling. Why would we read again if we just read all we could?
- Asyncio expects that tasks block the event loop for long enough time that polling should be preferred.
  This strategy only helps when something already went wrong (the event loop is clogged), but by always going with it
  it makes the event loop less efficient.

Conclusion:
Strategies that help avoid going bad should be always preferred over strategies that help when it already went wrong.
