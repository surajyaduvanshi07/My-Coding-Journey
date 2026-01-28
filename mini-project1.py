def add_student():
    my_list = []
    name = input("Enter Your Name : ")
    rollno = int(input("Enter your Roll no. : "))
    
    num_subject = int(input("Enter your Sujbect Number you want to add: "))
    my_list.append(name)
    my_list.append(rollno)
    data_line = f"Name: {name} | Rollno.: {rollno} "

    i = 1
    while i <= num_subject:
        subject = input(f"Enter your Subject {i} name: ")
        marks = float(input(f"Enter your {subject} marks = "))
        my_list.append(subject)
        my_list.append(marks)
        data_line += f" | {subject} = {marks}"
        i += 1
    with open("My-Coding-Journey/Student.txt","a") as f:
        f.write(data_line+"\n")

    print("✅ Student added successfully!\n")


def view_student():
    with open("My-Coding-Journey/Student.txt","r") as f:
        data = f.read()
        print(data)


def search_student():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open("My-Coding-Journey/Student.txt", "r") as f:
            for line in f:
                if search_name in line:
                    print("✅ Student Found:")
                    print(line.strip())
                    found = True

        if not found:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("No student records found.")



def delete_student():
    delete_name = input("Enter name to delete: ").lower()
    found = False

    try:
        with open("My-Coding-Journey/Student.txt", "r") as f:
            lines = f.readlines()

        with open("My-Coding-Journey/Student.txt", "w") as f:
            for line in lines:
                if delete_name not in line.lower():
                    f.write(line)
                else:
                    found = True

        if found:
            print("🗑 Student record deleted.")
        else:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("No student records found.")
    


while True:
    print("1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice : ")
    if (choice == "1"):
        add_student()
    elif(choice == "2"):
        view_student()
    elif(choice == "3"):
        search_student()
    elif(choice == "4"):
        delete_student()
    elif(choice == "5"):
        break
    else:
        print("Invalid choice")