#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space).

first_name = input("Please enter your first name: ")
print(f"{first_name} is {len(first_name)} characters long. ")
surname = input("Please enter your surname: ")
print(f"{surname} is {len(surname)} characters long." )

print(first_name + " " + surname)
