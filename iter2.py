scores=[1,5,7]

print("loop")
for s in scores:
    print(s)

print("Iterator")#LAZY
try:
    si=iter(scores)#iterable
    print(next(si))#1 #iterator
    print(next(si))#5
    print(next(si))#7
    print(next(si))#StopIteration
except StopIteration:
    print("Can't read further")