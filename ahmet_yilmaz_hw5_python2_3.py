## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Date of completion: 2 hours
##The question has 2 parts. First I have to find the user age and calculate it in days and weeks and display the output clearly. In second part, I have to calculate the distance a car will travel in different hours and display each of them clearly  

### Ask the user to enter his/her age

age = int(input( "Enter  your age: " ))
##Calculate the age in days and weeks

ageDays= age*365

ageWeeks= age*52

##Output the age in days and age in weeks

print ("Your age in days is:", ageDays)
print ("Your age in weeks is:", ageWeeks)

##part 2

##The car is travelling 55 miles per hour
speed= 55
##The time the car will travel in is 3,6 and 10 hours
for time in [3,6,10]:
##Display the distance the car will travel in 3,6 and 10 hours
    print ( " The distance the car will travel in {} hours is: {:.2f} miles" .format(time,speed*time))

