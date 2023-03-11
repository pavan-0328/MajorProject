import pymongo

myclient = pymongo.MongoClient("mongodb+srv://root:root@majorapp.tnk70j0.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient['mernapp']
mycol = mydb['number_plate']



for i in mycol.find({"number_plate":"GXIS OGJ"}):
    print(i)