import time
import types
import datetime

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
        yield i, item
        t2 = time.time()
        total_time_elapsed = t2 - t1
        cycle_count = i + 1
        avg_cycle_time = total_time_elapsed / cycle_count
        cycles_remaining = length - cycle_count
        time_remaining = avg_cycle_time * cycles_remaining
        print "Estimated Time Remaining: %d mins." % (time_remaining / 60)

def enumerate_with_etc(iterable):
    """Iterate over iterable and estimate the time of completion.

    Print out an initial estimate after either 10 iterations or 10% of the
    iterations. Print out subsequent estimates when the estimate has changed
    significantly since the last time an estimate was printed out (more than
    10% of the total estimated run time)"""

    if isinstance(iterable, types.GeneratorType):
        iterable = list(iterable)
    length = len(iterable)
    last_est = None
    sig_diff = None
    t1 = datetime.datetime.now()
    print "Start Time: {0}".format(t1.isoformat())
    for i, item in enumerate(iterable):
        yield i, item
        t2 = datetime.datetime.now()
        cycles = i + 1
        pc_complete = float(cycles) / length
        cycles_remaining = length - cycles
        total_time_elapsed = t2 - t1
        avg_cycle_time = total_time_elapsed / cycles
        time_remaining = avg_cycle_time * cycles_remaining
        best_est = datetime.datetime.now() + time_remaining
        total_est_time = best_est - t1
        if last_est:
            est_diff = abs(best_est - last_est)
            sig_diff = est_diff > est_diff / 10
        if ((not last_est and (cycles > 10 or pc_complete > 0.1)) or sig_diff):
            last_est = best_est
            print "Estimated Time of Completion: {0}".format(
                last_est.isoformat())
    print "Actual Time of Completion: {0}".format(
        datetime.datetime.now().isoformat())

