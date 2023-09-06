#Check values are in given range
def validate_credits(credit):
    return credit in (0,20,40,60,80,100,120)

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

print("Staff Version with Histogram\n")

#Loop while user inputs are Correct
while True: 
    try:
        pass_credits = int(input("Enter your total PASS credits :"))
#Identify validate_credits function to check user inputs at pass_credits are in correct range
        if not (validate_credits(pass_credits)): 
#If user inputs at pass_credits are not in correct range 
            print("Out of range") 
        else:
#If only above condition is true continue from this
            defer_credits = int(input("Enter your total DEFER credits:")) 
#Identify defer_credits are in correct range
            if not (validate_credits(defer_credits)): 
#If user inputs at defer_credits are not in correct range
                print("Out of range")
            else:
#If only above condition is true continue from this
                fail_credits = int(input("Enter your total FAIL credits :")) 
#Identify fail_credits are in correct range
                if not (validate_credits(fail_credits)): 
#If user inputs at fail_credits are not in correct range
                    print("Out of range")
                elif pass_credits + defer_credits + fail_credits != 120:
#Assume that Out of range error prompt first and prints only one error form both of total and range errors
                    print("Total incorrect") 
#Checks all the user input values are in given range and summation is 120        
                elif validate_credits(pass_credits) and validate_credits(defer_credits) and validate_credits(fail_credits) and pass_credits + defer_credits + fail_credits == 120: 
            
#If only above condition is true continue from this
                    if pass_credits == 120: 
                        print("Progress")
                        progress_count += 1
                    elif pass_credits == 100:
                        print("Progress (module trailer)")
                        trailer_count += 1
                    elif fail_credits != 80 and fail_credits != 100 and fail_credits != 120:
                        print("Do not progress – module retriever")
                        retriever_count += 1
                    else:
                        print("Exclude")
                        exclude_count += 1

                    user_input = input("Would you like to enter another set of data?\n(Enter 'y' for yes or 'q' to quit and view results)\nEnter your option:")
                    if user_input.lower() == "q":
                        
#Get the summation of the counts 
                        sum_count = [progress_count, trailer_count, retriever_count, exclude_count] 
                        
#Vertical Histogram
                        
#Use for to get printing star counts in below for loop
                        v_histogram_count_list = [progress_count, trailer_count, retriever_count, exclude_count] 
                        print("\n----------------------------------------------")
#Vertical histogram 
                        print("\nProgress | Trailing | Retriever | Excluded") 
                                 
#Repeats till max of the count
                        for i in range(max(v_histogram_count_list)): 
#Passing progress_count,trailer_count,retriever_count,exclude_count values to the for loop
                            for j in range(4): 
                                if v_histogram_count_list[j] > 0:
#If one of the count != 0 print a star
                                    print("   *       ", end="") 
                                else:
                                    print("           ", end="") 
                                v_histogram_count_list[j] -= 1 
                            print()
                            i += 1
                        print("\n")
#Summation of the counts
                        print(sum(sum_count), "outcomes in total.\n") 
#Exit from the loop and the program with a correct outcome when user inputs are correct
                        break 

#If user not input an integer print integer required
    except ValueError:
        print("Integer required")



# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1870997

# Date: 07/12/2021
        
