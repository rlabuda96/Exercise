variable_one=int(input("First variable is:"))
variable_two=int(input("Second variable is:"))
variable_three=int(input("Third variable is:"))
variable_summary=variable_one+variable_two+variable_three

if variable_one == variable_two and variable_one == variable_three and variable_two == variable_three :
    variable_summary_three_times=variable_summary*3
    print("All variable's are the same, continue calculations...")
    print(variable_summary_three_times)
else :
    print("Sum these three numbers are: ", variable_summary)