# Python import scenarios

##Example 1

Folder structure:
```
example/project1:
    |--module1.py
    |--resource1.txt
    |--main.py
example/project2:
    |--main.py
```

And the files: 

example/project1/module1.py:
```
...
    path = './resource1.txt'
    with open(path, 'r') as file: 
        a = file.read() 
...
```

example/project1/main.py:
```
import module1.py
```

example/project2/main.py:
```
sys.path.append('path/project1')
import module1.py
```

if the current working directory is "path/project1" then
running "python main.py" runs fine, but if we try to run the same file from any other
directory it will break because './resource1.mat' is only valid within "path/project1".
Likewise if we switch to path/project2, and try to run "python main.py" it will also 
break for the same reason.

Using __init_paths.py would only help with that, if inside each __init_path we also defined the absolute paths of the resources that will be used inside the current project:

```
resource1_path = osp.join(this_dir, '../data/resource_location/resource1.mat')
resource2_path = osp.join(this_dir, '../data/resource_location/resource2.npy')
```

## Example 2

For example in the previous scenario we could have instead:
```
example_with_init_paths_diff_names/project1:
    |--_init_paths_project1.py
    |--module1.py
    |--resource1.mat
    |--main.py
example_with_init_paths_diff_names/project2:
    |--_init_paths_project2.py
    |--main.py
```

example_with_init_paths_diff_names/project1/_init_paths_project1.py:
```
...
resource1_path = correct_path('resource1.txt')
...
```

example_with_init_paths_diff_names/project1/module1.py:
```
from _init_paths_project1 import resource1_path
open(resource1_path)
```

example_with_init_paths_diff_names/project1/main.py:
```
import module1.py
```

example_with_init_paths_diff_names/project2/_init_paths_project2.py:
```
...
add_path(correct_path('../project1'))
...
```

example_with_init_paths_diff_names/project2/module2.py:
```
import _init_paths_project2
import module1

def func2():
    print(f"Func2 calling project1.func1: {module1.func1()}")

if __name__ == "__main__":
    func2()

```

example_with_init_paths_diff_names/project2/main.py:
```
import _init_paths_project2, module2
import module1
```

Like that we can run:
* python project1/main.py
* python project2/main.py
* python project2/module2.py
without any issues and regardless of the current working directory.

_init_paths_project1.py and _init_paths2_project2.py have different names cause otherwise, when within module1.py we try to import 
resource1_path, python looks inside project2/_init_paths.py and not project1/_init_paths.py which causes an error.



## Example 3 

Finally we could have:
```
example_with_init_paths/project1:
    |--main.py
    |--project1_lib
        |--_init_paths.py
        |--module1.py
        |--resource1.txt
example_with_init_paths/project2:
    |--main.py
    |--project2_lib
        |--_init_paths_project2.py
        |--module2.py
    
```
example_with_init_paths/project1/project1_lib/_init_paths.py:
```
resource1_path = correct_path('resource1.txt')
```

example_with_init_paths/project1/project1_lib/module1.py:
```
from . import _init_paths

def func1():
    path = _init_paths.resource1_path
    with open(path, 'r') as file: 
        a = file.read() 
    return a
```

example_with_init_paths/project1/main.py:
```
from project2_lib import _init_paths, module2
from project1_lib import module1
```

example_with_init_paths/project2/project2_lib/_init_paths.py:
```
add_path(correct_path('../../project1'))
```
example_with_init_paths/project2/project2_lib/module2.py:
```
from . import _init_paths
from project1_lib import module1

def func2():
    print(f"Func2 calling project1.func1: {module1.func1()}")


if __name__ == "__main__":
    func2()
```

example_with_init_paths/project2/main.py:
```
from project2_lib import _init_paths, module2
from project1_lib import module1

```

Like that we can run:
* python project1/main.py
* python project2/main.py
* python -m project2.project2_lib.module2   
    (if we don't call module2 as a module we get:  "ImportError: attempted relative import with no known parent package", 
    because of the relative import "from . import _init_paths" inside module2.py   ) 

 









	
	 
