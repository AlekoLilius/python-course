

# ideas
# gives suggestion for which car the user means if it's not in the list of cars
# 

def main():

    print('''
:::::::::::::::::::::::::::
::: Car Loan Calculator :::
:::::::::::::::::::::::::::''')

    valid_actions = '123456'
    while True:
        print('''
      :::        Menu        :::
      ::: 1. List Contacts   :::
      ::: 2. Search Contact  :::
      ::: 3. Add Contact     :::
      ::: 4. Update Contact  :::
      ::: 5. Remove Contact  :::
      ::: 6. Exit Program    :::
              ''')
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n        === Invalid Action ===")
            continue

        match action:
            case '1' : pass
            case '2' : pass
            case '3' : pass
            case '4' : pass
            case '5' : pass
            case '6' : break

if __name__ == '__main__':
    main()