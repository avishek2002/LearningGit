# This is the first program file of our project. It was created in the Update1.0 branch.
# Later we opened a pull request and merged it to the main branch.

# Update1.1 extended to check if name is valid or not.

# user inputs first name and last name
fname = input("Enter your first name : ")
lname = input("Enter your last name : ")
if (len(fname) == 0 or len(lname) == 0):
	print("ERROR! First name and/or last name cannot be left empty!")
else:
	print("Hello, " + fname + " " + lname)
