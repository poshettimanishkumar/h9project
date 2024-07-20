class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def sas(c,name,age):
       return c(name,age)
p1=person.sas("mayank",19)
print(p1.name)
print(p1.age)
