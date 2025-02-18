
# Hometask2


#2.1
FullName=input("Enter your full name: ")
ReverseName=FullName[::-1]
print(f"Reversed name is :{ReverseName}")


#2.2
full_name = input("Please enter your full name (last name first): ")
parts = full_name.split()

if len(parts) >= 2:
    first_name = parts[1]
    reversed_first_name = first_name[::-1]
    print(f"Your first name in reverse order is: {reversed_first_name}")
else:
    print("Please enter your name in the correct format: 'LastName FirstName'")
