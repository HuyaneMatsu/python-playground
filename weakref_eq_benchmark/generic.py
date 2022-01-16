from scarletio import WeakReferer
from timer import timer, LOOP_COUNT

class WeakReferableType():
    __slots__ = ('__weakref__')


OBJECT_1 = WeakReferableType()
OBJECT_2 = WeakReferableType()

REFERENCE_1 = WeakReferer(OBJECT_1)
REFERENCE_2 = WeakReferer(OBJECT_2)


def eq_weak(reference, object_):
    return reference == WeakReferer(object_)

def eq(reference_1, reference_2):
    return reference_1 == reference_2


def main_loop():
    for _ in range(LOOP_COUNT):
        eq_weak(REFERENCE_1, OBJECT_1)
        eq_weak(REFERENCE_1, OBJECT_2)
        eq(REFERENCE_1, REFERENCE_2)


def main():
    # heat up
    main_loop()
    
    with timer():
        main_loop()


main()
