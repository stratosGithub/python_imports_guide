import os 
import sys

this_dir = os.path.dirname(os.path.realpath(__file__))

def correct_path(path):
    return os.path.realpath(os.path.join(this_dir, path))

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

resource1_path = correct_path('resource1.txt')
