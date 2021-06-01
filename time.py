import time
mins = 0
secs = 0
timer = ""
while True:
    secs = int(secs)
    mins = int(mins)
    time.sleep(1)
    if(secs < 60):
        secs = secs + 1
    if(secs == 60):
        secs = 0
        mins = mins + 1
    secs = str(secs)
    mins = str(mins)
    timer = mins + ":" + secs
    writer = open("timer.txt", "w")
    writer.write(timer)
    
    print(timer)
    
