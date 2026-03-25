def bold(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>"+func()+"</i>"
    return wrapper

@bold
@italic
def greet():
    return "Good Morning"

print(greet())
##############################################
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                print(func())
        return wrapper
    return decorator

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@repeat(2)
@uppercase
def say():
    return "Hello"


##################################

import time

print(time.time())
say()
print(time.time())