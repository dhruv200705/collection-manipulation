
students = {}

print("Welcome to the Student Data Organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":

        print("\nEnter student details:")

        student_id = input("Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
            continue

        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        students[student_id] = {
            "Name": name,
            "Age": age,
            "Grade": grade,
            "Date of Birth": dob,
            "Subjects": subjects
        }

        print("Student added successfully!")

    
    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\nAll Student Records:")

            for student_id, details in students.items():

                print("\nStudent ID:", student_id)

                for key, value in details.items():
                    print(key + ":", value)

   
    elif choice == "3":

        student_id = input("Enter Student ID: ")

        if student_id in students:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Grade")
            print("4. Update Date of Birth")
            print("5. Update Subjects")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                students[student_id]["Name"] = input("New Name: ")

            elif update_choice == "2":
                students[student_id]["Age"] = input("New Age: ")

            elif update_choice == "3":
                students[student_id]["Grade"] = input("New Grade: ")

            elif update_choice == "4":
                students[student_id]["Date of Birth"] = input("New DOB: ")

            elif update_choice == "5":
                students[student_id]["Subjects"] = input("New Subjects: ")

            else:
                print("Invalid choice!")
                continue

            print("Student information updated!")

        else:
            print("Student not found!")

   
    elif choice == "4":

        student_id = input("Enter Student ID: ")

        if student_id in students:

            del students[student_id]

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    
    elif choice == "5":

        subjects = []

        for details in students.values():

            student_subjects = details["Subjects"].split(",")

            for subject in student_subjects:

                subject = subject.strip()

                if subject and subject not in subjects:
                    subjects.append(subject)

        if len(subjects) == 0:
            print("No subjects available.")

        else:
            print("\nSubjects Offered:")

            for subject in subjects:
                print("-", subject)

    # Exit
    elif choice == "6":

        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")
