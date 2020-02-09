#!usr/bin/python3.8

# generate your secure password 
# simple script with python

import random
import os
import platform

if platform.system() == 'Windows':
	os.system("cls")
else:
	os.system("clear")

print('''\33[92m
         _           _                _     _
        | |         | |              | |   (_)
   __ _ | | __ __ _ | |_  ___  _   _ | | __ _
  / _` || |/ // _` || __|/ __|| | | || |/ /| |
 | (_| ||   <| (_| || |_ \__ \| |_| ||   < | |
  \__,_||_|\_\\__,_| \__||___/ \__,_||_|\_\|_|

			By Hedi_Smiri ^_^

~~ Press Help For Details ~~
==============================================
''')
def generated(x,diff) :

	# Diffucult list
	list1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghkmoiup+0123456789iorzeyuhgfdbvc_-'.,;:!?@&|(){}[]/\<># "
	# Easy List
	list2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	# choice List From input User
	if diff == 'e':
		list = list2
	else:
		list = list1
	# Generate Password With Random
	pwd =""
	for i in range(0,x):
		pwd +=random.choice(list)
	return pwd

# PP Program
while True :
	try:
		rep = str(input(">\33[91m "))
		if (rep == "start"):
			print ("\33[92m==============================================")
			print ('[+] Genereate Your owen Password ')
			length = input ("[+] Length of Password : \33[91m")
			print("\33[92m")
			if length == "exit" :
				print ("Thankes for using it ^_^")
				break
			while True:
				Diff = str(input("[+] Difficult of Password Easy or Hard E\H : \33[91m")).lower()
				print("\33[92m")
				if (Diff in ['e','h']):
					break
			print ("[+] Your Password is : \33[91m" , generated(int(length),Diff))
			print("\33[92m")
		elif rep == "help":
			print ('''\33[92m
     start = start the script Generate Your PasswOrd
     exit  = exit the script
     help  = Guide of script
			''')
		elif rep == "exit":
			break
		else :
			print("Soory i dont undreasted :(")
	except:
		print("Check Your Input ")