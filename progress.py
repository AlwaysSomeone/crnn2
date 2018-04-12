import sys, time

for i in range(1000):
    if i%100 == 0:
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()  ##随时刷新到屏幕上
