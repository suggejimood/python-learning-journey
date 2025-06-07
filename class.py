class FirstClass:
    x = 5

obj = FirstClass()
print(obj.x)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"STR: Name: {self.name} Age: {self.age}"
    
    def login(self):
        print("Password is true. Welcome", self.name)

newUser = User("John", 36);
print(f"Name: {newUser.name} Age: {newUser.age}")

print(newUser)
newUser.login()

del newUser.name
del newUser