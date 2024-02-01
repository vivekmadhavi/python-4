#wapp to ask for the name and den welcome

name=input("enter ur name")

if name == "":
	print("u did not enter the name ")
elif not name.isalpha():
	print("name should only contain alphabets")
elif name.strip() == "":
	print("name can not contain only space")
elif len(name) < 2:
	print("name shud be atlest 2 letter ")
else:
	msg = "good morning " + name
	print(msg)