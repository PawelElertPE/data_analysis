import time
from datetime import datetime

i = 0
while True:
    print("keep coding in python dude")
    time_before = time.time()
    time.sleep(3.5)
    time_after = time.time()
#    time_array = time.localtime(local_time)
    print(round(time_after - time_before, 5))
    i += 1
    print(f"The loop has been executed {i} times")
    current_time = datetime.now().time()
    print(f"The current time is: {current_time}")
    
    
