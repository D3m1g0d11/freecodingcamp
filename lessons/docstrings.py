#Docstrings
"""Docstrings help descript the work.
    docstrings.py does .............


    -Dog

"""
def increment(n):
    """Increment a number"""
    
    
class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
        
    def bark(self):
        """Let the dog bark"""
        print('WOOF!')
        
print(help(Dog))