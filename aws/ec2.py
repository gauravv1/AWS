#!/usr/bin/python
import boto3
import subprocess

ec2 = boto3.client('ec2')

def list_ec2():
	response = ec2.describe_instances()
	for reservation in response["Reservations"]:
		for instance in reservation["Instances"]:
			print("Instance ID is: % s" % instance["InstanceId"])
		        for i in response["Reservations"]:
                		for x in i["Instances"]:
					state = (x["State"])
					print("Instance State is: % s" % state['Name'])

def desc_ec2():
	instance = raw_input("Enter Instance id for which you want to get details:")
	response = ec2.describe_instances(InstanceIds=[instance])
	for i in response["Reservations"]:
		for x in i["Instances"]:

			print("Instance ID is: % s" % x["InstanceId"])
			state = (x["State"])
			print("Instance State is: % s" % state['Name'])
			print("Instance Public DNS is: % s" % x["PublicDnsName"])
			print("Instance Type: % s" % x["InstanceType"])
			print("Public IP is: % s" % x["PublicIpAddress"])
			print("Private IP is: % s" % x["PrivateIpAddress"])

def maint():
	instance = raw_input("Enter the instance name which you want to stop or start:")
	x = ec2.describe_instances(InstanceIds=[instance])
	for i in x["Reservations"]:
		for x in i["Instances"]:
			state = (x["State"])
			state_status = state['Name']
			print(state_status)

			if state_status != 'running' and state_status != 'stopped':
				print("Instance is either terminated or in pending state")
			else:
				if state_status == 'stopped':
					ans = raw_input("Instance is already stopped. Do you want to start it[Y/N]:").lower()
					if ans == 'y':
						ec2.start_instances(InstanceIds=[instance])
						print("Instance is started now")
					else:
						print("Instance is not started")
				else:
					ans = raw_input("Instance is running. Are you sure you want to stop it[Y/N]:").lower()
					if ans =='Y':
						ec2.stop_instances(InstanceIds=[instance])
						print("Instance is running")
					else:
						print("Instance is started")

###########Starting EC2 Menu#################

message='''Welcome to EC2 Menu:
        1. List Instances
        2. Instance Details
        3. Start/Stop Instance
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
        list_ec2()
elif    main_choice == 2:
        desc_ec2()
elif    main_choice == 3:
        maint()
elif    main_choice == 4:
	print 'Good Bye!'        
else:
        print("Please enter correct choice")

##########End of EC2 menu###############

