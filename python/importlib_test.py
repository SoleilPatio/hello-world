import sys
import pathlib
import importlib

def LoadPythonModule( python_src_file ):
    py_src = pathlib.Path(python_src_file)
    sys.path.append(str(py_src.parent))    #add module directory to  path
    module_name = py_src.stem
    module = importlib.import_module(module_name)
    return module

