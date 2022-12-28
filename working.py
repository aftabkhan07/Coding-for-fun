class Person :
    
    def __init__(self,name,age,place):
        self.name=name
        self._age=age            # _ is protected can be used in subclass 
        self.__place=place       # __ is private can use in subclass
    
    def __str__(self):
        return "person object"
        
    def year(self,num):
        print(f"you are {str(self._age - num)} year old")

class Person1(Person):
    
    def __init__(self,name,age,place,car):
        super().__init__(name,age,place)
        self.car=car

    def years(self):                # See below line vishnu can we like do it without hardcoding 8 
        years=super().year(num)       # Here we were not able to call it outside the class so we hard coded 8 in it 
        return (f"you are {years} old")

person = Person1("aftab",23,"Mumbai",True)  
person.years()