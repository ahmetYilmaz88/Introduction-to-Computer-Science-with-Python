## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Date of completion: 2 hours
##The question has 2 parts. First I will ask the user number of checks and display total fee. Checking fee must be formatted to 2 digits after the decimal point. In part 2, I will ask the user filing status and income and compute it to the income tax.
##get the number of checks 
fee=0
##how many checks you have    
numChecks=int(input( " Enter the number of checks: " ))

              
##if the number given less than or equal to 0, message an error

while numChecks<1:
        print ("number is not accepted")
        print (" try again")

        numChecks=int(input( " Enter the number of checks: " ))


##calculate the fee by using the decision statement
        
else:
    if numChecks < 20:
        fee= 8+(numChecks*.09)
    elif numChecks >= 20 and numChecks <= 39:
        fee= 8+(numChecks*.07)
    elif numChecks >= 40 and numChecks <= 59:
        fee= 8+(numChecks*.06)
    elif numChecks >=60:
        fee= 8+(numChecks*.05)

##print the output
    print ( " Your fee is {:.2f} : " .format(fee) )

   

##part 2

             
##ask the user for filing status              
filingStatus= input( "What is your filing status? married or single? " )
##if the answer is not "single" or "married" give an error message

if filingStatus != "married" and filingStatus != "single":
    while filingStatus != "married" and filingStatus != "single":
        print (" answer should be only single or married " )

        filingStatus= input( "What is your filing status? married or single? " )    
##ask the user for income
income= int(input( " Enter your income: " ))
    

while income<0:
        print( " you can not enter a negative income ")

        income= int(input( " Enter your income: " ))
        
##        calculate the income tax
else:

    if filingStatus=="married" and income >=0 and income <= 50000:
        total=income*.05
        print ("your income tax is {:.2f} : ".format(total))
    elif filingStatus=="single" and income >=0 and income <= 50000:
        total=income*.07
        print ("your income tax is {:.2f} : ".format(total))
    elif filingStatus=="married" and income >=50000 and income <= 100000:
        total=(income-50000)*.08+2500
        print ("your income tax is {:.2f} : ".format(total))
    elif filingStatus=="single" and income>=50000 and income <= 100000:
        total=(income-50000)*.12+2500
        print ("your income tax is {:.2f} : ".format(total))
    elif filingStatus=="married" and income >100000:
        total=(income-100000)*.1+6000
        print ("your income tax is {:.2f} : ".format(total))
    elif filingStatus=="single" and income >100000:
        total=(income-50000)*.15+2500
        print ("your income tax is {:.2f} : ".format(total))
                  


