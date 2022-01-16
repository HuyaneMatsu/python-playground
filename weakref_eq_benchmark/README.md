Benchmark for overwriting weakreferer's `__eq__` for fast comparisons.

Cpython3.8
```
$ python3 forwarded_eq.py 
Task finished in 0.2524 seconds.
$ python3 generic.py 
Task finished in 0.2008 seconds.
```

pypy3.6
```
pypy3 generic.py 
Task finished in 0.0883 seconds.
pypy3 forwarded_eq.py 
Task finished in 0.0036 seconds.
```

The results show, that in cpython the time spent executing bytecode slows our process dramatically down. But in pypy
tells us, that our solution is way better than the generic `__eq__`.

In Cpython deeper analysis shows, that our `__eq__` function only gets slower when we compare 2 references. So
operations with alive objects should be still fine.
