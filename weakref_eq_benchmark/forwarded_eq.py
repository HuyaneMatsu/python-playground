from scarletio import WeakReferer
from timer import timer, LOOP_COUNT

class WeakReferableType():
    __slots__ = ('__weakref__')


class ForwardedEqWeakReferer(WeakReferer):
    __slots__ = ()
    
    def __eq__(self, other):
        object_ = self()
        if (object_ is not None):
            return other == object_
        
        if isinstance(other, ForwardedEqWeakReferer):
            return WeakReferer.__eq__(self, other)
        
        return False


OBJECT_1 = WeakReferableType()
OBJECT_2 = WeakReferableType()

REFERENCE_1 = ForwardedEqWeakReferer(OBJECT_1)
REFERENCE_2 = ForwardedEqWeakReferer(OBJECT_2)


def eq(object_1, object_2):
    return object_1 == object_2


def main_loop():
    for _ in range(LOOP_COUNT):
        eq(REFERENCE_1, OBJECT_1)
        eq(REFERENCE_1, OBJECT_2)
        eq(REFERENCE_1, REFERENCE_2)


def main():
    # heat up
    main_loop()
    
    with timer():
        main_loop()


main()
