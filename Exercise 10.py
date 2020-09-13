variable=int(input("Type an integer"))
summary=variable+(variable*variable)+(variable*variable*variable)
print(summary)

variable_one=int("%s" %variable)
variable_two=int("%s%s" %(variable,variable))
variable_three=int("%s%s%s" %(variable,variable,variable))
print(variable_one)
print(variable_two)
print(variable_three)

print(variable_one+variable_two+variable_three)