def store():
    for i in range(1000000):
        print("hi")
        yield i#generator

res=store()
#for i in res:
#    print(i)

print(next(res))
print(next(res))
print(next(res))
