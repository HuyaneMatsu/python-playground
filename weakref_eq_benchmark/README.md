Benchmark for overwriting weakreferer's `__eq__` for fast comparisons.

Cpython3.8
```
$ python3 forwarded_eq.py 
Task finished in 0.4162 seconds.
$ python3 generic.py 
Task finished in 0.3140 seconds.
```

pypy3.6
```
$ pypy3 generic.py 
Task finished in 0.1362 seconds.
$ pypy3 forwarded_eq.py 
Task finished in 0.0059 seconds.
```

The results show, that in cpython the time spent executing bytecode slows our process dramatically down. But in pypy
tells us, that our solution is way better than the generic `__eq__`.

In Cpython deeper analysis shows, that our `__eq__` function only gets slower when we compare 2 references. So
operations with alive objects should be still fine.
