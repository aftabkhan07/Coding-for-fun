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

