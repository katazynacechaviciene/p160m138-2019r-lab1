import sys 

def greet (name: str):
    print (f"Hello, {name}!")
    return f"Hello, {name}!"
greet(sys.argv[1])
