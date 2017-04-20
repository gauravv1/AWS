#!/usr/bin/python



message = '''Welcome to Main Menu:
        1. IAM User Management
        2. EC Instance Management
        3. Volume Management
        4. Exit'''
print(message)

is_valid = 0
main_choice = 0

while not is_valid :
        try :
                main_choice = int ( raw_input('Enter your choice [1-3] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
if main_choice == 1:
        import iam
elif    main_choice == 2:
        import ec2
elif    main_choice == 3:
        import volume
elif    main_choice == 4:
        print("Goodbye")
else:
        print("Please enter correct choice")


