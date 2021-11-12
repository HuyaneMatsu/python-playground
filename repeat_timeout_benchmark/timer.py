import sys
from time import perf_counter
from contextlib import contextmanager

LOOP_COUNT = 100000

@contextmanager
def timer():
    """
    Times the execution of the capsulised code.
    
    This function can be used within a context block.
    """
    start = perf_counter()
    try:
        yield
    finally:
        end = perf_counter()
        sys.stdout.write(f'Task finished in {end-start:.04f} seconds.\n')
