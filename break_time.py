import webbrowser
import time

start_time = time.ctime()

print("This Program is started on "+ start_time)

total_breaks = 3
wait_time = 2 # Seconds


for i in range(0,total_breaks):
    time.sleep(wait_time)
    webbrowser.open("https://www.youtube.com/watch?v=ZHDtda9K36c")