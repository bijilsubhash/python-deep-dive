# timing.py

print(f'loading timing.py: __name__ = {__name__}')

"""
Times how long a snippet of code takes to run
over multiple iterations.
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'reps elapsed average')

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)

if __name__ == '__main__':
    # get code and repeats from command line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help='The Python code snippet to time.')
    parser.add_argument('-r', '--repeats', type=int, default=10, help='The number of times to repeat the code snippet.')
    args = parser.parse_args()

    print(f'timing: {args.code}...')
    result = timeit(args.code, args.repeats)
    print(result)
    print(f'{result.average:.6f} seconds per loop')

