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

carrie = {
    "student_id": "1010",
    "first_name": "Carrie",
    "last_name": "Wholesome"
}

print("\n  -- INSERT STATEMENTS --\n")
carrie_student_id = students.insert_one(carrie).inserted_id
print("  Inserted student record Carrie into the students collection with document_id "
 + str(carrie_student_id))

carrie_search = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1010 -- \n")

print("  Student ID: " + carrie_search["student_id"] + 
"\n  First Name: " + carrie_search["first_name"] + 
"\n  Last Name: " + carrie_search["last_name"] + "\n")

carrie_delete = students.delete_one({"student_id": "1010"})

new_student_list = students.find({})
 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")

for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + 
    "\n  First Name: " + doc["first_name"] + 
    "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")