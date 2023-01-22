Testing new scarletio timeout logic speed.

In this benchmark we measure 4 different stats:
- `timeout <= 0.0`
- `timeout > 0.0`
- `future already done`
- `future completes before timeout`

The new scarletio timeouting not only provides different api, but contain 2 optimisation for 2 out of the 4 cases:
- `timeout <= 0.0`
- `future already done`

Using cpython3.8
```py
Starting asyncio benchmark
Task finished in 1.5647 seconds.
Task finished in 3.1185 seconds.
Task finished in 2.0739 seconds.
Task finished in 2.6711 seconds.
Starting scarletio old benchmark
Task finished in 1.1250 seconds.
Task finished in 1.8044 seconds.
Task finished in 0.4028 seconds.
Task finished in 0.9428 seconds.
Starting scarletio new benchmark
Task finished in 0.3001 seconds.
Task finished in 1.7225 seconds.
Task finished in 0.0855 seconds.
Task finished in 0.8100 seconds.
```

Using cpython3.11
```py
Task finished in 1.1172 seconds.
Task finished in 2.6465 seconds.
Task finished in 1.2244 seconds.
Task finished in 1.5079 seconds.
Starting scarletio old benchmark
Task finished in 0.7350 seconds.
Task finished in 1.4880 seconds.
Task finished in 0.3035 seconds.
Task finished in 0.4651 seconds.
Starting scarletio new benchmark
Task finished in 0.2775 seconds.
Task finished in 1.5599 seconds.
Task finished in 0.0609 seconds.
Task finished in 0.4366 seconds.
```

Using pypy
```py
Starting asyncio benchmark
Task finished in 0.3738 seconds.
Task finished in 0.7547 seconds.
Task finished in 0.3088 seconds.
Task finished in 0.4752 seconds.
Starting scarletio old benchmark
Task finished in 0.3725 seconds.
Task finished in 0.7142 seconds.
Task finished in 0.0996 seconds.
Task finished in 0.2089 seconds.
Starting scarletio new benchmark
Task finished in 0.2347 seconds.
Task finished in 0.8228 seconds.
Task finished in 0.0183 seconds.
Task finished in 0.2352 seconds.
```

The statistics show that:
- `timeout <= 0.0` Around 3 times faster in cpython (all) and 0.66x in pypy.
- `timeout > 0.0` Stagnated in cpython (all) and got around 10% worse in pypy.
- `future already done` Around 5 times faster in cpython (all) and 4 times faster in pypy.
- `future completes before timeout` Stagnated in cpython (all) and got around 10% worse in pypy.

The fact that on pypy the performance dropped on non-edge cases will require further investigation.

Conclusion
The edge case checking provides great speedup when we are actually at an edge case.
