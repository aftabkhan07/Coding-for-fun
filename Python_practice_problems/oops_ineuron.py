import pymongo
class mongodb : 
    
    def __init__(self , userid1 , password1, data ) :
        
        """
        this is a code for mongodb connectivity and its related application 
        """
        self.userid = userid1
        self.password = password1 
        self.data = data 
    
    
    def connect(self) :
        print("this fun will help you to coonnect with your mongo db ")
        url = "mongodb+srv://" + self.userid + ":" + self.password+ "@cluster0.qivyyos.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        return client
        
    def insert(self ):
        conn = self.connect()
        print("this fun will help you to insert into mondo db ")
        db = conn['mongodb_test']
        coll = db['mongo_record']
        coll.insert_one(self.data)
        
    def update(self):
        print("this fun will help you to update in mongodb")


mongo = mongodb("mongodb" , "mongodb")

mongo.insert({'name' : "sudhanshu" , "number" : 234324324})

######################################################################

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
        years=super().year(8)       # Here we were not able to call it outside the class so we hard coded 8 in it 
        return (f"you are {years} old")

person = Person1("aftab",23,"Mumbai",True)
person.years()

person._age              #name mangling for protected
person._Person__place    #name mangling for private
person.car

#############################################################################

class test1 : 
    @staticmethod
    def meth1():
        return "this is a meth you can access without creating an object " 
    
    def meth2(self) : 
        return "this is a meth withouit static " 
b = test1()
test1.meth1()

########################################################################

class test5:
    def test(self) : 
        return "this is my test meth" 
    
class test6:
    def test(self) :
        return "this is my meth from calss test6 called test" 
    
class test7(test5):
    def test(self) : 
        return "this is my test form test7"  
var_classtest7 = test7()
var_classtest7.test()

# 'this is my test form test7'

class test8:
    
    def test(self , c = 5 , b = 4 , d = 7 ):
        return c,b,d

var_test8  = test8()
var_test8.test()
(5, 4, 7)
var_test8.test("sudh")
('sudh', 4, 7)
var_test8.test("sudh" , "kumar")
('sudh', 'kumar', 7)

# orverlaoding is a situation where number of argument and data type will be different 
# overrding is a situation where signature of the function means name and parameter will same we will just chage the def of the func





