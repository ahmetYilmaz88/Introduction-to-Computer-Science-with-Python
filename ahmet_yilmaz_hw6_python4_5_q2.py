## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Date of completion: 2 hours
##The question is about entering several numbers of assignment scores and 3 exam scores. Finding the average and displaying the grade.


total=0

##how many assignments
num=int(input( "Enter number of assignments: "))

##use a for loop to allow to prompt the number of assignments
for x in range(1,num+1):
    assignmentScore=float(input("Enter the  assignment score: "))
    
##use a while loop to allow user enter again if the score less than 0 and greater than 100    
    while assignmentScore<0 or assignmentScore>100:
        print( " I can not accept scores less than 0 and greater than 100 ")
        assignmentScore=float(input("Enter the  assignment score: "))
    total=total+assignmentScore

##calculate the average of assignment scores
avg=total/num

##input the exam and final scores and use a while loop to allow user enter again if the score less than 0 and greater than 100    

exam1 = int(input("Enter the score for exam 1: "))
while exam1<0 or exam1>100:
    print( " I can not accept scores less than 0 and greater than 100 ")
    exam1 = int(input("Enter the score for exam 1: "))


exam2 = int(input("Enter the score for exam 2: "))
while exam2<0 or exam2>100:
    print( " I can not accept scores less than 0 and greater than 100 ")
    exam2 = int(input("Enter the score for exam 2: "))
final = int(input("Enter the score for final exam: "))
while final<0 or final>100:
    print( " I can not accept scores less than 0 and greater than 100 ")
    final = int(input("Enter the score for final exam: "))

##calculate the average of all scores
average = float((avg*.65)+(exam1*.1)+(exam2*.1)+(final*.15))

##enter a grade value regarding to syllabus 
if average >= 94 and average<= 100:
    grade= "A"
elif average >= 90 and average< 94:
    grade= "A-"
elif average >= 87 and average< 90:
    grade= "B+"
elif average >= 84 and average< 87:
    grade= "B"
elif average >= 80 and average< 84:
    grade= "B-"
elif average >= 77 and average< 80:
    grade= "C+"
elif average >= 74 and average< 77:
    grade= "C"
elif average >= 70 and average< 74:
    grade= "C-"
elif average >= 67 and average< 70:
    grade= "D+"
elif average >= 64 and average< 67:
    grade= "D"
elif average >= 60 and average< 64:
    grade= "D-"
elif average <60 and average >=0:
    grade= "F"

##Display the outputs
print ( " Total number of assignment scores is : ", x )
print ( " Total number of exams is : ", 2 )
print ( " Total number of final exam is : ", 1 )
print ( " The average is : {:.2f} "  .format(average) )
print ( " Your grade is: ", grade)
