from pymongo import MongoClient

URL = "mongodb+srv://admin:admin@cluster0.2vo3rgq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(URL)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ]\n")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + 
    "\n  First Name: " + doc["first_name"] + 
    "\n  Last Name: " + doc["last_name"] + 
    "\n")


result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Brewster"}})

freed = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 -- \n")

print("  Student ID: " + freed["student_id"] + 
"\n  First Name: " + freed["first_name"] + 
"\n  Last Name: " + freed["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")