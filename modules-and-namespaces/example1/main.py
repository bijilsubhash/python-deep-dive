import sys

print("============================================")
print("Running main.py - module name: {0}".format(__name__))

import module1

print("imported module1 again")
del globals()['module1']

import module1

module1.pprint_dict("main.globals", globals())

print("============================================")
