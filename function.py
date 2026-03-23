def show():
    print("Hello CGI")

show()

#WAP to create add fx which takes 2 params and returns the sum
def add(a,b):
    #print(type(a),type(b))
    total=0
    try:
        total=a+b
    except TypeError:
        print("only int is allowed")
    except Exception as ex:
        print("all errors are handled")
    return total

res=add(2,"3")
print(res)

print("Done")