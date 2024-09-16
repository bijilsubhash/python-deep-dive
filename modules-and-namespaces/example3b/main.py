import sys

import importer

module1 = importer.import_module('module1', 'module1_source.py', './modules-and-namespaces/example3b')

print("sys.says", sys.modules.get('module1', 'module1 not found'))

module2 = importer.import_module('module2', 'module2.py', './modules-and-namespaces/example3b')

module2.hello()

print("sys.says", sys.modules.get('module2', 'module2 not found'))