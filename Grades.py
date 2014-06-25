#Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. If the score is between 
#0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message
#and exit. For the test, enter a score of 0.85.

grades = raw_input("Enter your score:")
try:
    grade = float(grades)
except:
    grade = -1
if grade>1.0:
    print 'Enter your score as a decimal'
elif grade>=.9:
    print 'A'
elif grade>=.8:
    print 'B'
elif grade>=.7:
    print 'C'
elif grade>=.6:
    print 'D'
elif grade<.6:
    print 'F'
elif grade==-1:
    print 'Not a number'