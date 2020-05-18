print("Hello World")

def __mul__(self, other, unexpected):  # Noncompliant. Too many parameters
     return 42

def __add__(self):  # Noncompliant. Missing one parameter
    return 42
    
# TODO


class SomeClass:
    lookUp = false
    def lookup():       # Non-compliant; method name differs from field name only by capitalization
        pass