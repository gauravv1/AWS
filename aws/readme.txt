This code is desined to automate basic AWS tasks like managing EC2 instance, managing IAM and volumes management. 

1. main.py is the main code which will provide main menu and will call deifferent modules based on the choice of operations. 
2. iam module is for basic IAM realted operations like list users, create user or delete user. 
3. ec2 module is for EC2 instances related operations like list instances, instance details, start or stop instance and rename the instance. 
4. volume module works on list volumes, create volume, delete volumes, attach or detach volume from instance and volume snapshot management. 


Note: This code currently work only for US-EAST-1 (N.Virginia). You need to give the admin role to the EC2 hosts where these scripts need to run. Access keys or secure access keys is not going to work.  

Resources:

boto3
python 2
