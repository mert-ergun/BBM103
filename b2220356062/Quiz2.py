# Importing SYS library for using "sys.argv" list for command line arguments.
import sys


# Defining a function named "Health Status" for problem 2. We can call this function later. This is a fruitful function
# that returns a value to us. We will not print that value because function itself will print it in command line.
def healthStatus(height, mass):
    if height <=0:
        print("Please enter a valid height!")
        exit()
    bmi = mass / (height**2)
    if bmi < 18.5:
        return "Your BMI is {} and you are Underweight".format(int(bmi))
    elif bmi < 24.9:
        return "Your BMI is {} and you are Healthy".format(int(bmi))
    elif bmi < 30:
        return "Your BMI is {} and you are Overweight".format(int(bmi))
    else:
        return "Your BMI is {} and you are Obese".format(int(bmi))


# Starting with "Try" command, if user enters a value that is not integer, instead of Value error,
# it will give my commit.
try:
    # Computing "Score" from given values using sys.argv list. sys.argv[0] is name of file, sys.argv[1] is 2-point shots
    # sys.argv[2] is 3-point shots and sys.argv[3] is 1-point faul shots.
    score = int(sys.argv[1])*2 + int(sys.argv[2])*3 + int(sys.argv[3])
    # Finally printing score in form of "Integer".
    print(score)
except ValueError:
    print("Please use integers for shots!")
except IndexError:
    print("Please enter 3 integers.")
# Written by b2220356062 Mert ERGÜN
