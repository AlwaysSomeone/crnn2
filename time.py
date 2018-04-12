import datetime
import sys
import time

starttime = datetime.datetime.now()

#long running

for i in range(10):
    if i%100 == 0:
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()  ##随时刷新到屏幕上
        time.sleep(0.5)
for i in range(10):
    sys.stdout.write(str(i) + " ")
    sys.stdout.flush()  ##随时刷新到屏幕上
    time.sleep(0.5)

endtime = datetime.datetime.now()

print((endtime - starttime).seconds)