import time
import types

def enumerate_with_etr(iterable, length=None, start=0, stop=None):
    if isinstance(iterable, types.GeneratorType):
        iterable = list(iterable)
    if not length:
        length = len(iterable)
        if not stop:
            stop = length
        length = length - start - (length - stop)
    t1 = time.time()
    for i, item in enumerate(iterable[start:stop + 1]):
        cycle_t1 = time.time()
        yield i, item
        cycle_t2 = time.time()
        cycle_time = cycle_t2 - cycle_t1
        total_time_elapsed = cycle_t2 - t1
        cycle_count = i + 1
        avg_cycle_time = total_time_elapsed / cycle_count 
        cycles_remaining = length - cycle_count
        time_remaining = avg_cycle_time * cycles_remaining
        print "Estimated Time Remaining: %d mins." % (time_remaining / 60)
