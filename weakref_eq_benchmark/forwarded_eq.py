from scarletio import WeakReferer
from timer import timer, LOOP_COUNT

class WeakReferableType():
    __slots__ = ('__weakref__')


class ForwardedEqWeakReferer(WeakReferer):
    def __eq__(self, other):
        object_ = self()
        if (object_ is not None):
            return other == object_
        
        return WeakReferer.__eq__(self, other)


OBJECT_1 = WeakReferableType()
OBJECT_2 = WeakReferableType()

REFERENCE_1 = ForwardedEqWeakReferer(OBJECT_1)
REFERENCE_2 = ForwardedEqWeakReferer(OBJECT_2)

def eq(object_1, object_2):
    return object_1 == object_2


def main_loop():
    for _ in range(LOOP_COUNT):
        eq(OBJECT_1, REFERENCE_1)
        eq(OBJECT_2, REFERENCE_1)
        eq(REFERENCE_2, REFERENCE_1)


def main():
    # heat up
    main_loop()
    
    with timer():
        main_loop()


main()
