#To check values are in given range
def validate_credits(credit):
    return credit in (0,20,40,60,80,100,120)

progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

try:
 #To input user inputs(marks order in list as pass_credits,defer_credits,fail_credits)
    user_inputs = [[120,0,0], [100,0,20], [80,20,20], [60,0,60], [40,0,80]]
                
    for i in range(len(user_inputs)): #Asign the those into pass_credits,defer_credits,fail_credits
        pass_credits,defer_credits,fail_credits = user_inputs[i]
        
        if not (validate_credits(pass_credits)) and (validate_credits(defer_credits)) and (validate_credits(fail_credits)): #Calling validate_credits function to check user inputs at pass_credits are in correct range
            print("Out of range - range error in value of index",i,"-",user_inputs[i])#If user inputs at fail_credits are not in correct range print "Out of range"
            break
        elif pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect in value of index",i,"-",user_inputs[i]) #Assume that Out of range error prompt first and prints only one error form both of total and range errors
            break
        elif validate_credits(pass_credits) and validate_credits(defer_credits) and validate_credits(fail_credits) and pass_credits + defer_credits + fail_credits == 120: #Checks all the user input values are in given range and summation is 120        
                
            if pass_credits == 120: #If only above condition is true continue from this
                print("Progress",pass_credits,',',defer_credits,',',fail_credits)
                progress_count += 1
            elif pass_credits == 100:
                print("Progress (module trailer)",pass_credits,",",defer_credits,",",fail_credits)
                trailer_count += 1
            elif fail_credits != 80 and fail_credits != 100 and fail_credits != 120:
                print("Do not progress – module retriever",pass_credits,",",defer_credits,",",fail_credits)
                retriever_count += 1
            else:
                print("Exclude",pass_credits,",",defer_credits,",",fail_credits)
                exclude_count += 1
        
        #Horizontal Histrogram
    else:
        print("\n------RESULTS-------")
        print("\n""Horizontal Histogram")
        print("Progress", progress_count, " : ", "*" * progress_count)
        print("Trailing", trailer_count, " : ", "*" * trailer_count)
        print("Retriever", retriever_count, ":", "","*" * retriever_count)
        print("Excluded", exclude_count, " : ", "*" * exclude_count, "\n")

        count_list = [progress_count, trailer_count, retriever_count, exclude_count]
                        
        print(sum(count_list), "outcomes in total.\n") #Print sum of the counts
                        
except ValueError:
    print("Integer required") #If user not input an integer print integer required



# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1870997

# Date: 07/12/2021

    
