def fibonacci(till):
    #a=0
    #b=1
    #OR
    a,b=0,1
    for i in range(till):
        yield a
        a,b=b,a+b
        #OR
        #a=b
        #b=a+b

f=fibonacci(15)

for i in f:
    print(i,end=" ")

print("\n")
#=========second way
def fibo():
    a,b=0,1
    while True:#infinite loop
        yield a
        a,b=b,a+b

gen=fibo()

for g in gen:
    if(g>100):
        break
    print(g,end="\t")