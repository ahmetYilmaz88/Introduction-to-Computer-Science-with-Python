## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Time of completion: 2 hours
##The coding is about writing a set of age values to a file and finding lowest highest and average age 
highest = -100000 
lowest = 100000 
average =0
total = 0
x=0
##create a file
myfile = open("file.txt", "w")

##ask the user the number of data item for age values
x=int(input( " enter the number of data items for age values: "))

##create a for loop to ask user for their age and use try except block to to display error message
for i in range (x):
    
    flag = True
    while flag == True:
        try:
            age = int(input(" Please enter your age: "))
            flag = False
        except ValueError:
            print( " invalid value " )
##  calculate the age in days and write it into the file      
    ageDays= age*365
    myfile.write("age in Years = " + str(age))
    myfile.write("age in Days = " + str(ageDays))

##find the lowest, highest and average age
    if age>highest:  
        highest = age
    if age<lowest:
        lowest = age
    total = total + age

    
    average= total/x

##write all the outputs in to the file
myfile.write( " highest age is = " + str(highest))

myfile.write( " lowest age is = " + str(lowest))

myfile.write( " average age is = " + str(average))
 

##close the file
myfile.close()



    
