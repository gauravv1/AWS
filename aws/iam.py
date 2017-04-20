#!/usr/bin/python
import boto3
iam = boto3.client('iam')

##########functions#########################

def user_list():		#This function list the IAM users.
        user_list = iam.list_users(PathPrefix='/', MaxItems=5)
        print ("List of Users and their ARN is:")
        for i in user_list['Users']:
                print(i['UserName'], i['Arn'])

def create_user():
	uname = raw_input('Enter User Name:').lower()
	response = iam.create_user(
		UserName=uname,
	)	
	print("User %s created" % uname)
	

def delete_user():
	uname = raw_input('enter User Name to be deleted:').lower()
	print ("User %s will be deleted" % uname)
	choice = raw_input('"Are you sure Y/N:').lower()
	if choice in 'n':
		print('User %s is not removed:' % uname)
	else:
		response = iam.delete_user(
			UserName=uname
		)
		print ('User %s is deleted' % uname)

#########End of Funtions####################

###########Starting IAM Menu#################

message = '''Welcome to IAM Menu:
	1. List Users
	2. Create User
	3. Delete User
	4. Exit'''
print(message)

is_valid = 0

while not is_valid :
        try :
                main_choice = int ( raw_input('Enter your choice [1-3] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
if main_choice == 1:
	print user_list()
elif	main_choice == 2:
	create_user()
elif	main_choice == 3:
	delete_user()
elif	main_choice == 4:
	print("Goodbye")
else:
	print("Please enter correct choice")

##########End of IAM menu###############
