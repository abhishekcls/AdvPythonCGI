#class Emp:
#    pass

class Emp:
    def __init__(self,id=0,name="abc"):#constructor
        self.id=id
        self.name=name
    def show(self):
        #print("Hello ",self.name, "ID ",self.id)
        print(f"Hello {self.name} ID {self.id}")

e=Emp(101,"AAA")#Object/Instance
e2=Emp(102,"BBB")#Object/Instance
e.show()
e2.show()

class PartTimeEmp(Emp):#inheritance
    pass

p=PartTimeEmp()
p.show();
#Task