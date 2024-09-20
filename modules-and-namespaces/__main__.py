# run.py

import timing

code = '[x**3 for x in range(1_000)]'

result = timing.timeit(code, repeats=100)
print(result)

if __name__ == '__main__':
    print('run.py is being run directly')