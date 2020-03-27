import _init_paths_project1

def func1():
    path = _init_paths_project1.resource1_path
    with open(path, 'r') as file: 
        a = file.read() 
    return a


