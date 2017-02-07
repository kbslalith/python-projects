import random
import string

from numpy import sort

y = [1,2,3,4,5,6,7,8,9,10,11]

for i in range(0,11):

	y[i] = ''+"".join( [random.choice(string.letters[:26]) for p in xrange(6)])
	
print y
print sort(y)