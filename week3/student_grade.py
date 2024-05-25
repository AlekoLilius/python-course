
students = {}
subjects = {'English', 'Math', 'Swedish'}

def view_students():
    print('''
\n      :::      Students      :::
      :::    Name - Grade    :::\n''')
    for student in students:
        print(f"{student} - ", end='')
        for grade in students[student]:
            print(f" {grade[0]}: {grade[1]} ", end='')
        print('')

def present_average():
    avg_grades = []
    for student in students:
        avg_grade = 0
        for grade in students[student]:
            avg_grade += grade[1]
        avg_grade /= len(students[student])
        avg_grades.append((student, avg_grade))

    print("\n     ::: Name - Average Grade :::\n")
    for student in avg_grades:
        print(f"{student[0]} - {student[1]}")

def update_student(action):
    print(f"\n      ::: {action} Student :::\n")
    while True:
        name = input("Name (First & Last): ")
        if name.replace(' ', '').isalpha():
            break
        else:
            print("Wrong format!")
    if action == 'Add':
        if name in students:
            print("Warning! Student already in list.")
            return
    else:
        if name not in students:
            print("Warning! Student not in list.")
            return
    
    grades = []
    while True:
        try:
            for subject in sorted(list(subjects)):
                grade = int(input(f"Grade for {subject} (0-100): "))
                if grade < 0 or grade > 100:
                    raise Exception("Grade should be 0-100")
                grades.append((subject, grade))
            break
        except Exception as e:
            print('')
            print(e)
            print('')

    students[name] = grades

def remove_student():
    print("\n      ::: Remove Student :::\n")
    name = input("Name (First & Last): ")
    if name in students:
        del students[name]
        print(f"{name} deleted")
    else:
        print("Warning! Student not in list.")

def main():

    print('''
:::::::::::::::::::::::::::::::::::::::
::: Student Grade Management System :::
:::::::::::::::::::::::::::::::::::::::''')

    valid_actions = '123456'
    while True:
        print('''
      :::        Menu        :::
      ::: 1. View Students   :::
      ::: 2. Present Average :::
      ::: 3. Add Student     :::
      ::: 4. Update Student  :::
      ::: 5. Remove Student  :::
      ::: 6. Exit Program    :::
              ''')
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n        === Invalid Action ===")
            continue

        match action:
            case '1' : view_students()
            case '2' : present_average()
            case '3' : update_student('Add')
            case '4' : update_student('Update')
            case '5' : remove_student()
            case '6' : break

if __name__ == '__main__':
    main()