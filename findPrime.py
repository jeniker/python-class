# Jennifer King
# October 5, 2017
# This program searches through integers with the upper
# limit defined by the user, to find all the prime
# numbers and list them.

def makeList(n):  # Function to create a list of numbers for the sieve 
    fullList=[]   # to locate prime numbers starting at 3
    for i in range(3,n+1,2): # starts at 3, skips even numbers since they
        fullList.append(i)   # automatically are not prime
    return fullList  # this list ends at the upper limit selected by the user

def seive(n):  # Function to parse prime numbers from fullList
    print("Seive of Eratosthenes for values up to ", n)
    lineCount = 1  # Placeholder for the counter
    print("{0:5}".format(2),end="\t")  # prints 2 as a member of myList (prime numbers) and
                                       # makes 5 spaces after it for final formatting
    myList=makeList(n)  # defines that the data list is from the makeList function
    while(len(myList)!=0):  # starts iteration to go until there are no numbers left
        base=myList[0]  # defines where the base starts, at the first member of myList which is 3
        lineCount +=1  # moves to the next line
        print("{0:5}".format(base),end="\t")  # prints "3" 5 spaces apart 
        for i in range(1,int(n/base+1)):  # divides the upper limit of list by each member 
                                          # of the list starting at 3. This removes all the
                                          # multiples of each prime number as well.
             if(myList.count(i*base)>0):  # this removes non-prime numbers from list
               myList.remove(i*base)      
    if (lineCount % 9 == 0):              # this starts a new line of numbers making 9 columns
                      print()
                      
def main():  # function to obtain the upper limit from user and move this number to the 
     n = int(input("Enter upper prime limit to evaluate: "))  # sieve and makeList function
     seive(n)

main()
