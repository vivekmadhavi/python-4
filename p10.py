#wapp to read the string and check if they are anagtams
#two string having same letter but diff meaning

s1=input("enter first name")
s2=input("enter second name")

string1=sorted(s1)
string2=sorted(s2)

r1="".join(string1)
r2="".join(string2)
if r1==r2:
	print("is anagram")
else:
	print("invalid")