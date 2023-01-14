import sys
from time import process_time
from contextlib import contextmanager

@contextmanager
def timer():
    """
    Times the execution of the capsulised code.
    
    This function can be used within a context block.
    """
    start = process_time()
    try:
        yield
    finally:
        end = process_time()
        sys.stdout.write('Task finished in {:.04f} seconds.\n'.format(end-start))
