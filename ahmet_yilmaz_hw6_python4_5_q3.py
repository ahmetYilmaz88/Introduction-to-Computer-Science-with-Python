## My name: Ahmet Yilmaz
##Course number and course section: IS 115 - 1001 - 1003
##Date of completion: 2 hours
##The question has 4 parts. I need to write 4 functions in various problems.

##write a function to display a string of characters and the number of times.
def func1(char ,times):
    for i in range(times):
        print(char)

##write a function to return the total number of vowels.
def func2(text):
    lower_text = text.lower()

    count = 0
    for char in lower_text:
        if char in ('a', 'e', 'i', 'o', 'u') :
             count+=1
    return count

##write a function to  to return the decimal number equivalent to a given Roman numeral.
def func3(text):
    if text == "I":
        return 1
    elif text == "II":
        return 2
    elif text == "III":
        return 3
    elif text == "IV":
        return 4
    elif text == "V":
        return 5
    else: 
        return -1

##Write a function that accepts, as parameters, the values for acceleration and velocity and returns the length. 
def func4(acceleration, speed):
    if acceleration == 0.0:
        return -9999
    else:
        speed = speed**2
        acceleration = 2 * acceleration
        return  speed/acceleration

##test for all the functions    
def main():
    func1("Hello", 4)
    print (func2("Hello World"))

    tests = [
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("V", 5),
    ("VI", -1),
    ("HELLO", -1),
    ("", -1),
    ]

    for arg, expected in tests:
        result = func3(arg)
        print(arg, expected, '|', result, expected == result)

    tests = [
    (1, 1, 0.5),
    (1, 2, 2.0),
    (10, 2, 0.2),
    ]

    for arg1, arg2, expected in tests:
        result = func4(arg1, arg2)
        print(arg, expected, '|', result, expected == result)

main()
