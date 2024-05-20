
students = {}
grades = []


def add_student(name, grade):
    if name in students.keys():
        students[name] = grade
    else:
        students[name] = grade

def main():

    print('''
:::::::::::::::::::::::::::::::::::::::
::: Student Grade Management System :::
:::::::::::::::::::::::::::::::::::::::''')

    valid_actions = '12345'
    while True:
        print('''
      :::        Menu        :::
      ::: 1. View Students   :::
      ::: 2. Present Average :::
      ::: 3. Add Student     :::
      ::: 4. Remove Student  :::
      ::: 5. Exit Program    :::
              ''')
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n        === Invalid Action ===")
            continue

        

if __name__ == '__main__':
    main()