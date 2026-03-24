#Iterable
# list [] mutable(change)
# tuple () immutable(can't change)
# set {}

scores=[1,5,7,4,9,4]
print(scores)
scores.append(11)
print(scores)
print(type(scores))

scores2=(1,5,7,4,9,4)
print(scores2)
print(type(scores2))

scores3={1,5,7,4,9,4}
print(scores3)
print(type(scores3))