a="abc"
b="xyz"

print(a+b)

x=10
y=20

print(x+y)

class Height:
    def __init__(self,f,i):
        self.feet=f
        self.inch=i

    def __add__(self, other):
        t=Height(0,0)
        t.inch=self.inch+other.inch
        t.feet=self.feet+other.feet
        if t.inch>11:
            t.feet+=1
            t.inch=t.inch-12

        return t
    
    def __str__(self):
        return f"feet: {self.feet}, inches: {self.inch}"

h1=Height(4,5)
h2=Height(7,9)
print(h1)
print(h2)

h3=h1+h2
print(h3)
#Task1: subtraction
#Task2: inches must not be 12 or above it should be added in feet