# Program: CIS 110 Program 2
# Jennifer King
# September 9,2017
# A program that calculates a total weekly wage
# from user input of hourly wage and total hours
# it also tests for overtime (over 40 hours)
# and calculates the ot rate and adds it to weekly wage


def main(): # ask the user for the hourly wage and the total hours for the week
    hourlyWage = float(input("Enter your hourly wage: "))
    totalHours = int(input("Enter your total hours for the week: "))
    # test the total hours for eligilble overtime
    if totalHours > 40:
        otHours = (totalHours- 40)
        # caluclate the overtime by multiplying the hours over 40
        # by the hourly wage plus half the hourly wage
        totalPay = ((hourlyWage *1.5) * otHours) + (hourlyWage * 40)
        # or if there is no overtime calculate the wage by hours times hourly wage
    else: totalPay = (hourlyWage * totalHours)
    # print out the results for the user
    print("Your total weekly pay is $" + str(totalPay))
    
main()
    
