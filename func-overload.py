def add(a,b,c=0):
    print(a+b+c)

add(2,3)
add(2,3,4)

def sum(*args):
    total=0
    for i in args:
        total+=i
    print(total)

sum(2,3)
sum(2,3,5,6,8)

def show(a):
    print(a)

show("Abhishek")
show(100)
###############################################
from functools import singledispatch

@singledispatch
def process_data(data):
    print("Unsupported data type")


@process_data.register(int)
def _(data):
    print(f"Processing integer: {data*2}")

@process_data.register(list)
def _(data):
    print(f"Processing list of length: {len(data)}")

process_data(10)
process_data([1,4,6,9])
#######################################################
@singledispatch
def process_multi_data(*data):
    print("Unsupported data type")


@process_multi_data.register(int)
def _(*data):
    print(f"Processing integer: ")
    for d in data:
        print(d*2)

@process_multi_data.register(list)
def _(data):
    print(f"Processing list of length: {len(data)}")

@process_multi_data.register(str)
def _(data):
    print(f"Processing str of length: {len(data)}")

process_multi_data(10)
process_multi_data(10,20)
process_multi_data([1,4,6,9])
process_multi_data("abc")