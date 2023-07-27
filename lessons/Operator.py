class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('Eating dog food')
        
    def __gt__(self, other):
        return True if self.age > other.age else False
        