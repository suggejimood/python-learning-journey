def greet(name):
    print(f"Merhaba, {name}!")

greet("Mehmet")

square = lambda x: x ** 2

print(square(5))

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello World")
    
hello()