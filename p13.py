#wapp to read user name and password
#if useer name is kamal and paasword is claases
#then 0/p success else failure

from getpass import *
username=getpass("enter the username")
password=getpass("enter the password")

if (username =="kamal") and(password =="classes"):
	print("success")
else:
	print("fail")

#input()  echo
#getpass() non-echo