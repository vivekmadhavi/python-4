#waoo to read string and remove all blank space

s1=input("enter a string")
s2 = ""

for s in s1:
	if s != " ":
		s2 = s2 + s

print(s1)
print(s2)