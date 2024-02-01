#wapp to read the string and count
#1)alphabet 2)digit 3)others


string=input("enter the string")

al,di,ot = 0,0,0
for s in string:
	if s.isalpha():
		al=al+1
	elif s.isdigit():
		di=di+1
	else:
		ot=ot+1

print("al = ",al)
print("di = ",di)
print("ot = ",ot)