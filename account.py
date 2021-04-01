import os
clear=lambda:os.system('cls')
clear()
print("\n\n\t\t welcome to user management\t\t\n\n")

key=["name","email","password"]

userdetail={key[0]:"",key[1]:"",key[2]:""}

data=[]

def createAccount():
	import os
	clear=lambda:os.system('cls')
	clear()
	
	name=input("\n\n\t enter your name\n\n\t")
	email=input("\n\n\t enter your email\n\n\t")
	password=input("\n\n\t enter your password\n\n\t")
	
	userdetail [key[0]]=name 
	userdetail [key[1]]=email
	userdetail [key[2]]=password
	
	data.append(userdetail)
	

	print("\naccount creation success\n")
	
	input("enter main menu...")
	
	import os
	clear=lambda:os.system('cls')
	clear()
def loginDetails():
	import os
	clear=lambda:os.system('cls')
	clear()

	for d in data:
		if d[key[1]]== email and d[key[2]]== password:
			print("\n\n\t enter login successful \n\n\t")
		else:
			print("\n\n\t wrong key entered \n\n\t")

while True:

	print("\t\t 1.create new account...")
	print("\t\t 2.login with details...")
	print("\t\t 3.get user list...")
	print("\t\t 4.exit...")
	
	choice=int(input("\n\n\t enter your choice \n\n\t"))

	if choice==1:
		createAccount()
	elif choice==2:
		pass
	elif choice==3:
		pass
	elif choice==4:
		exit()
	else:
		print("\n\t wrong input entered....")
		input("\n\t enter to try again\n\t")
	import os
	clear=lambda:os.system('cls')
	clear()	