## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Date of completion: 2 hours
##The question is about converting the pseudocode given by instructor to the Python code.

##set the required values
count=1
activity= "RESTING"
flag="false"

##how many activities 
numact= int(input(" Enter the number of activities: "))

##enter the activities as number as numact that the user enter    
while count < numact:
    flag= " true "
    activity= input( "Enter your activity: ")
    
##display the activity
    if activity=="RESTING":
        print ( " I enjoy RESTING too ")
    else:
        print ("You enjoy " , activity)
        count=count+1
if flag== "false":
    print (" There is no data to process ")
