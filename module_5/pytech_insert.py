from pymongo import MongoClient

URL = "mongodb+srv://admin:admin@cluster0.2vo3rgq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(URL)

db = client.pytech

# Freds' data document
freed = {
    "student_id": "1007",
    "first_name": "Freed",
    "last_name": "Boisen"
}

# Johns' data document
john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Layer"
}

# Travis' data document
travis = {
    "student_id": "1009",
    "first_name": "travis",
    "last_name": "mimen"
}

students = db.students

# insert statements with output
print("\n  -- INSERT STATEMENTS --")
freed_student_id = students.insert_one(freed).inserted_id
print("  Inserted student record Freed into the students collection with document_id "
 + str(freed_student_id))

john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John into the students collection with document_id "
 + str(john_student_id))

travis_student_id = students.insert_one(travis).inserted_id
print("  Inserted student record Travis into the students collection with document_id "
 + str(travis_student_id))

input("Press any key to quit.")
