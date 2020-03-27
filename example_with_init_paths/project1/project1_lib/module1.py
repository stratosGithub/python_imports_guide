from . import _init_paths

def func1():
    path = _init_paths.resource1_path
    with open(path, 'r') as file: 
        a = file.read() 
    return a


