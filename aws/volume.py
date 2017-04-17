#!/usr/bin/python

import time
import boto3

vol = boto3.client('ec2')

def list_vol():

        a = vol.describe_volumes()
        print "Volume                State"
        for i in a['Volumes']:
            print i['VolumeId'],
            print i['State']


def vol_create():

        size = int(raw_input('Volume size in GB:'))
        az = raw_input('Availability zone:').lower()
        ty = raw_input('Volume type[Standard|IO1|GP2|SC1|ST1]:').lower()
        if ty == 'io1':
            iops = int(raw_input('Volume IOPs[100 to 20000]:'))
            v = vol.create_volume(Size=size,AvailabilityZone=az,VolumeType=ty,Iops=iops)
            print 'Volume Id:', v["VolumeId"]
            print "Volume Created"
        else:
            v = vol.create_volume(Size=size,AvailabilityZone=az,VolumeType=ty,)
            print 'Volume Id:', v["VolumeId"]
            print "Volume Created"


def vol_delete():

        volume = raw_input('Enter the volume id which need to be deleted:')
        a = vol.describe_volumes(VolumeIds=[volume])
        for j in a['Volumes']:
            for k in j['Attachments']:
                inst = k['InstanceId']

        for i in a['Volumes']:
            state = i['State']
            print state
        if state == 'in-use':
            print ("Volume is attached to an instance %s need to be detached first." % inst)
            d = raw_input("Do you want to detach the volume?[Y/N]:").lower()
            if d =='y':
                vol.detach_volume(VolumeId=volume,InstanceId=inst)
                time.sleep(5)
                vol.delete_volume(VolumeId=volume)
                print "Volume detached and deleted."
            else:
                print "Volume not deleted."
        else:
            ans = raw_input("Volume %s will be deleted, are you sure[Y/N]: " % volume).lower()
            if ans =='y':
                vol.delete_volume(VolumeId=volume)
                print "Volume deleted."
            else:
                print "Volume is not deleted."


def attach():

        i = raw_input('Want to attach or detach the volume[A/D]:').lower()
        if i == 'a':
            volume = raw_input("Enter Volume Id:")
            a = vol.describe_volumes(VolumeIds=[volume])
            for j in a['Volumes']:
                for k in j['Attachments']:
                    inst = k['InstanceId']
            for i in a['Volumes']:
                state = i['State']
            if state == 'in-use':
                print ("Volume attached to an instance %s." % inst)
                a = raw_input("Do you want to detach this volume[Y/N]:").lower()
                if a == 'y':
                    vol.detach_volume(VolumeId=volume,InstanceId=inst)
                    time.sleep(5)
                    print "Volume is detached now."
                else:
                    print "Volume is not detached."
            else:
                inst = raw_input("Enter instance name to which volume need to be attached:")
                dev = raw_input("Enter mount path(example:/dev/sdf):")
                vol.attach_volume(VolumeId=volume,InstanceId=inst,Device=dev)
                print 'Volume is attached to the instance now.'

        elif i == 'd':
                volume = raw_input("Enter volume id:")
                a = vol.describe_volumes(VolumeIds=[volume])
                for j in a['Volumes']:
                    for k in j['Attachments']:
                        inst = k['InstanceId']
                for i in a['Volumes']:
                    state = i['State']
                if state == 'in-use':
                    print ("Volume is attached to instance %s will be detached" % inst )
                    ans = raw_input("Are you sure[Y/N]:").lower()
                    if ans =='y':
                        vol.detach_volume(VolumeId=volume,InstanceId=inst)
                        time.sleep(5)
                        print "Volume is detached now."
                    else:
                        print "Volume is not detached."
                else:
                    print "Volume is already detached"

        else:
            print 'Good Bye!'


def snapshot():

        message='''Please select:
        1. Snapshot for all volumes.
        2. Snapshot for selected volume.
        3. Snapshot for running instances.
        4. Snapshot for all instances.
        5. Snapshot for selected instance'''

        print(message)

        is_valid = 0

        while not is_valid :
            try :
                choice = int(raw_input('Enter your choice[1-5]:'))
                is_valid = 1
            except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
        if choice == 1:
            print "Snapshot for all volumes"
        elif choice == 2:
            print 'Snapshot for selected volume'
        elif choice == 3:
            print 'Snapshot for running instances'
        elif choice == 4:
            print 'Snapshot for all instances'
        elif choice == 5:
            print 'Snapshot for selected instances'
        else:
            print "Please enter correct choice."
###########Starting volume Menu#################


message='''Volume Menu:
        1. List volume
        2. Create Volume
        3. Delete Volume
        4. Attach or Detach Volume
        5. Take volume snapshot
        6. Exit'''

print(message)

is_valid = 0

while not is_valid :
        try :
                main_choice = int ( raw_input('Enter your choice [1-3] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
if main_choice == 1:
        list_vol()
elif    main_choice == 2:
        vol_create()
elif    main_choice == 3:
        vol_delete()
elif    main_choice == 4:
        attach()
elif    main_choice == 5:
        snapshot()
elif    main_choice == 6:
        print 'Good Bye!'
else:
        print("Please enter correct choice")

