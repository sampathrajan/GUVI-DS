import pymongo
import os

try:
    name =input("Enter Name: ")
    tam =int(input("Enter Tamil Mark: "))
    eng =int(input("Enter English Mark: "))
    mat =int(input("Enter Maths Mark: "))
    sci =int(input("Enter Science Mark: "))
    soc =int(input("Enter Social Mark: "))

    tot=tam+eng+mat+sci+soc
    avg=tot/5
    print("Total: "+str(tot))
    print("Average: "+str(avg))

    val = {}
    val["Name"] = name
    val["Tamil"] = tam
    val["English"] = eng
    val["Maths"] = mat
    val["Science"] = sci
    val["Social"] = soc
    val["Total"] = tot
    val["Average"] = avg

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["student"]
    mycol = mydb["exam"]
    insert=mycol.insert_one(val)
    print("Marks for the Student '"+name+"' Registered.")

except Exception as err:
    print(err)





