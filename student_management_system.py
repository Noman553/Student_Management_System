# let's create a small student management system
#first create a variable which hold A empty list

students = []
#declare all the functions and add the data of the students in functions
def add_students_details(name , rollno , *marks , **details):
    students_details = {
        "name" : name,
        "Roll No" : rollno,
        "marks" : marks,
        "details" : details
    }
    students.append(students_details)

# now you need to generate the student one by one
def generate_students():
    for student in students:
        yield student

def search_students(studentrollno , index = 0 ):
    if index >= len(students): # base case
       return None
    if students[index]["Roll No"] == studentrollno:
        return students[index]
    return search_students( studentrollno, index+1)

# now let's try to delete the - some students data

def delete_student(del_std):
    student = search_students(del_std)
    if student:
        students.remove(student)
        print("the student is successfully removed")
    else:
        print("student not found")

# new let's update the sudent data

def update_rollno(rollno , new_rollno):
    student = search_students(rollno)
    if student:
        student ["Roll No"] =  new_rollno
        print("the rollno is updated")
    else:
        print("rollno not found")


# Add the data of all the students
add_students_details(
        "Ali",
        1,
        10, 20, 30,
        city="Lahore",
        age=20

    )
add_students_details(
        "Ahmed",
        2,
        20, 30, 40,
        city="Lahore",
        age=21

    )
add_students_details(
        "Asad",
        3,
        30, 40, 50,
        city="Lahore",
        age=22

    )

# call all the functions
print(" All the students data")
for student in generate_students():
    print(student)

print("search student:-")
print(search_students(2))
print("delete the Student:-")
delete_student(3)
print("Update the rollNo:-")
update_rollno(2 , 10)

