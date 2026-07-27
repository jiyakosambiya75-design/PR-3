students=[]
def add_student():
    student_id=int(input("Student ID: "))
    if student_id == "ID" :
      print("Student id already exist.")
      return
    name=input("Name: ")
    age=int(input("Age: "))
    grade=input("Grade: ")
    dob=input("Date of Birth (YYYY-MM-DD): ").split()
    dob=tuple(dob)
    subject=input("Subjects(comma-separated): ")
    student={
        "ID" : student_id,
        "Name": name,
        "Age": age,
        "Grade": grade,
        "DOB": dob,
        "Sub": subject
        }
    students.append(student)
    print("Student added Successfully")
def display_student():
  if len(students)==0:
     print("No stuent found.")
     return
  for student in students:
   print(f"""
         Student ID : {student['ID']}
         Name : {student['Name']}
         Age : {student['Age']}
         Grade : {student['Grade']}
         DOB : {student['DOB']}
         Subject : {student['Sub']}
       """
         )
def update_student():
    ID=int(input("Enter student id to update: "))
    for student in students:
       if student["ID"]==ID :
        student["Name"]=input("Enter updated name: ")
        student["Age"]=int(input("Enter updated age: "))
        student["Sub"]=input("Enter updated Subject: ")
        
        print("student updated Successfully.")
        return
    print("ID not found")
    
def delete_student():
    ID=int(input("Enter student ID to remove: "))
    for student in students:
        if student["ID"] == ID :
            students.remove(student)
            print("student deleted Successfully!!!")
            return
        print("Student not exist.")

def displaysubjects_student():
    ID=int(input("Enter student ID: "))
    for student in students:
        if student["ID"] == ID :
            print(f"subjects: {student["Sub"]}")

print("Welcome to the student data organizer!")

while True:
    print("\nSelect an option: ")
    print("1. Add student")
    print("2. Display All Students")
    print("3. Update student Information")
    print("4. Delete Student ")
    print("5. Disply Subject Offered ")
    print("6. Exit ")      
    choice=int(input("Enter your choice: "))

    if choice == 1:
       add_student()
    elif choice == 2:
       display_student()
    elif choice == 3:
       update_student()
    elif choice == 4:
       delete_student()
    elif choice == 5:
       displaysubjects_student()
    elif choice == 6:
       print("Thank you for using the student Data organizer!!!")
       break
    else:
       print("Invalid choice...")
       
