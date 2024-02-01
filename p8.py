#wapp to read the string and count
#1)upper 2)lower  3)digit 4)others


string=input("enter the string")

lc,uc,di,ot = 0,0,0,0
for s in string:
	if s.islower():
		lc=lc+1
	elif s.isupper():
		uc=uc+1		
	elif s.isdigit():
		di=di+1
	else:
		ot=ot+1

print("lc = ",lc)
print("uc = ",uc)
print("di = ",di)
print("ot = ",ot)