from . import _init_paths
from project1_lib import module1

def func2():
    print(f"Func2 calling project1.func1: {module1.func1()}")

if __name__ == "__main__":
    func2()

