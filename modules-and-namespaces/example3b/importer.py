print('Running importer.py')

import os.path
import types
import sys

def import_module(module_name, module_file, module_path):

    if module_name in sys.modules:
        return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # read source code from file
    with open(module_rel_file_path, 'r') as code_file:
        source_code = code_file.read()
        
    # create a module object
    module1 = types.ModuleType(module_name)
    module1.__file__ = module_abs_file_path

    # set a ref to the global namespace (dictionary)
    sys.modules[module_name] = module1

    # compile source code and create byte code
    compiled_code = compile(source_code, filename=module_abs_file_path, mode='exec')

    # execute the compiled code
    exec(compiled_code, module1.__dict__)

    return sys.modules[module_name]