import os
import shutil,  errno
import random
from random import randint
import string
from numpy import sort

src = '/home/kbslalith/python projects/original message'
dst ='/home/kbslalith/python projects/secret message'

#os.makedirs('/home/kbslalith/python projects/secret message')

### Delete the secret message folder if already exists###

shutil.rmtree(dst)



def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
			print "AM HERE"
        else: 
			raise
			print "Am here too"
	os.remove(".DS_Store")

def create_secret_message():
	zero = 0
	prank_file = os.listdir(dst)

	saved_path = os.getcwd() 
	os.chdir(dst) 
	
	### Write a code to create 11 random words###

	y = [1,2,3,4,5,6,7,8,9,10,11,12]
	for i in range(0,12):
		y[i] = ''+"".join( [random.choice(string.letters[:26]) for p in xrange(6)])

	
	
	### Write a code to sort them###
	
	y_sorted = sort(y)
	
	###Write a code to rename the existing files with these sorted names###
	for name in sort(prank_file):
		
		if name.startswith('.'):
			print ""
		else:
			os.rename(name,str(randint(0,100))+y_sorted[zero]) 
			zero += 1
			print name
	
	### Write a code to attach random number to the starting ###
		


	os.chdir(saved_path) 
	

copyanything(src, dst)	

create_secret_message()	


'''

	i = 0
	file_names = []
	#print len(prank_file)
	for name in prank_file:
		#print name.split()
		file_names.append(name.split())
		#os.rename(file_name,file_name.translate(None,"0123456789")) 
	
	print (file_names)
'''