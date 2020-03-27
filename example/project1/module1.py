def func1():
    path = './resource1.txt'
    with open(path, 'r') as file: 
        a = file.read() 
    return a


