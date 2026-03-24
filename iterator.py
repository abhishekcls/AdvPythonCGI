#Iterator -> __next__()
'''
scores=[1,5,7,4,9,4]

print("loop")
for s in scores:
    print(s)

print("Iterator")#LAZY
si=iter(scores)#iterable
print(next(si))#1 #iterator
print(next(si))#5
print(next(si))#7
'''
nums=[]
def store():
    for i in range(1000000):
        nums.append(i)
    return nums

res=store()
it=iter(res)
for i in it:
    print(i)