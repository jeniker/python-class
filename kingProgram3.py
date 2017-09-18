# Program 3
# Jennifer King
# September 17, 2017
# A program that takes in a series of numbers from the user
# and instructs the user to press "enter" to end the input.
# The program then prints the sum, product and average of the
# user's numbers.

def main(): # ask the user for the numbers they want added, multiplied
            # and averaged. Instruct the user to press enter twice
            # to complete entering numbers.
    
    sum = 0.0                  # initialize the variable sum
    product = 1.0              # initialize the variable product
    average = 0.0              # initialize the variable average
    count = 0                  # initiale the loop count at 0
                               # obtain the numbers from the user                              
    data = input("Enter the numbers you want. Hit enter to stop entering numbers.")
    while data != "":          # test for the end condition of hitting enter to stop
        count +=1              # set the counter for each number the user enters
        number = float(data)   # change the input from string to float so we can do math
        sum += number          # add each number as it is entered for the sum
        product *= number      # multiply each number as it is entered for the product
        average = sum / count  # divide the sum by the total count for the average
                               # continue getting user input until user stops by hitting enter
        data = input("Enter the numbers you want. Hit enter to stop entering numbers.")        
    print("The sum is: ", sum) # print the sum of the user input numbers
    if sum == 0.0:             # test if the user entered no numbers- to fix the product to 0
        product = 0.0    
    print("The product is: ", product)      # print the product of the user input numbers
    print("The average is: ", average)      # print the average of the user input numbers
                        
main()
    
