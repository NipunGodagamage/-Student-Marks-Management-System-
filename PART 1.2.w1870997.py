# Check the values are in the given range
def Validate_credits(Credit):
    return credit in (0,20,40,60,80,100,120)
#Loop untill user inputs are correct 
while True:
    try:
        pass_credits=int(input("Please enter your pass credit: "))
#Identify validate_credits function to check user inputs at pass_credits are in correct range
        if not (validate_credits(pass_credits)): 
#If user inputs at pass_credits are not in correct range print "Out of range"
            print("Out of range")
        else:
#If only above condition is true continue from this
            defer_credits = int(input("Please enter your credit at defer:")) 
#Identify validate_credits function to check user inputs at defer_credits are in correct range
            if not (validate_credits(defer_credits)): 
#If user inputs at defer_credits are not in correct range print "Out of range"
                print("Out of range")
            else:
#If only above condition is true continue from this
                fail_credits = int(input( "Please enter your credit at fail :")) 
#Identify validate_credits function to check user inputs at fail_credits are in correct range
                if not (validate_credits(fail_credits)): 
#If user inputs at fail_credits are not in correct range print "Out of range"
                    print("Out of range")
                elif pass_credits + defer_credits + fail_credits != 120:
#Assume that Out of range error prompt first and prints only one error form both of total and range errors
                    print("Total incorrect") 
#Checks all the user input values summation is 120 
                elif validate_credits(pass_credits) and validate_credits(defer_credits) and validate_credits(fail_credits) and pass_credits + defer_credits + fail_credits == 120:        
#If only above condition is true continue from this            
                    if pass_credits == 120: 
                        print("Progress")
                    elif pass_credits == 100:
                        print("Progress (module trailer)")
                    elif fail_credits != 80 and fail_credits != 100 and fail_credits != 120:
                        print("Do not progress – module retriever")
                    else:
                        print("Exclude")
#Exit from the loop and the program with a correct outcome when user inputs are correct                        
                    break 

#If user not input an integer print "integer required"
    except ValueError:



# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1870997

# Date: 07/12/2021



        
