#Write a program to prompt the user for hours and rate per hour 
#using raw_input to compute gross pay. Pay the hourly rate for the hours
#up to 40 and 1.5 times the hourly rate for all hours worked above 40 
#hours. Use 45 hours and a rate of 10.50 per hour to test the program 
#(the pay should be 498.75). You should use raw_input to read a string 
#and float() to convert the string to a number. Do not worry about error
#checking the user input - assume the user types numbers properly.

hrs = raw_input("Enter Hours:")
h = float(hrs)
pay = raw_input("Enter Pay:")
p = float(pay)
if h>40.0:
    ovt = (40*p)+((h-40)*(p*1.5))
    print ovt
elif h<=40.0:
    reg_pay = h*p
    print reg_pay