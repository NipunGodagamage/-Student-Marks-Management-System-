#Input the number of credits at pass, defer and fail
pass_credits = int(input( "Please enter your Pass credit: "))
defer_credits = int(input("Please enter your Defer credit: "))
fail_credits = int(input( "Please enter your Fail credit: "))

if pass_credits == 120:
    print("Progress")
elif pass_credits == 100:
    print("Progress (module trailer)")
elif fail_credits != 80 and fail_credits != 100 and fail_credits != 120:
    print("Do not progress – module retriever")
else:
    print("Exclude")


# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1870997

# Date: 07/12/2021
