"""
os.listdir("Enter the folder url") => This will give you all the file names in a directory

os.getcwd() => This will give you the current working directory 

os.chdir("ENTER THE NEW DIR HERE") => Changes the Directory to user specified

os.rename(OLD NAME, NEW NAME) => Used to rename the file names

name.translate("","WHAT ALL DO YOU WANT TO REMOVE) => This will help you remove the bits you dont want
from a file name, in this case numbers

Remember to change the directory back to where you found it. easy way is to save it in a variable and use the same
"""

import os
dst ='/home/kbslalith/python projects/secret message'

def rename_files():
	prank_file = os.listdir(dst)

	saved_path = os.getcwd() 
	os.chdir(dst) 

	for file_name in prank_file:
		os.rename(file_name,file_name.translate(None,"0123456789")) 
	
	os.chdir(saved_path) 

rename_files()	