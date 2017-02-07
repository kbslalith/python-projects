"""
time.ctime() => this is used to find the current start time including date and day
time.sleep(ENTER SECONDS HERE) => This is used to make the program wait for few seconds
webbrowser.open("Enter URL Here") => This is used to pop open a web browser 
"""


import webbrowser
import time

def break_time():
	start_time = time.ctime()

	print("This Program is started on "+ start_time)

	total_breaks = 3
	wait_time = 2 # Seconds


	for i in range(0,total_breaks):
    		time.sleep(wait_time)
    		webbrowser.open("https://www.youtube.com/watch?v=ZHDtda9K36c")

break_time()
