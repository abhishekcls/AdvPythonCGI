#Decorator -> is a function that wraps another function to extend or modify 
# its behaviour without changing its code

def mydecorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@mydecorator
def dummy():
    print("Hi")

dummy()
#OR
def demo():
    print("Hello")

demo2 =mydecorator(demo)
demo2()

#Task -> find out the execution time of a fx using decorator