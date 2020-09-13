variables = input("Type the coma separates numbers: ")

#list = list(variables)
#tuple = tuple(variables)


list = variables.split(",")
tuple = tuple(list)

print("List : ", list)
print("Tuple : ", tuple)