class Demo:
    def __init__(self,name,desig):
        #public
        #self.name=name
        #self.desig=desig

        #private
        self.__name=name
        self.__desig=desig

    def __str__(self):
        return f"Name={self.__name} Designation={self.__desig}"
    
    def show(self):
        print(f"Name={self.__name} Designation={self.__desig}")

d=Demo("Abhishek","Trainer")
print(d)
#print(d.__name,d.__desig)#error because they are private
d.show()