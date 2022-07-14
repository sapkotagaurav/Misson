
import time
import psutil


import sys
import importlib
import os
t1 = time.time()
try:
    f = sys.argv[1]
    os.system('python3 '+f)
    t2= time.time()
    print()
    print()
    print("File Name:",f)
    print("Time Taken:" ,(t2-t1)*1000,"ms")
    print(psutil.Process(os.getpid()).memory_info().rss/1024/1024, "mb")
except IndexError:
    print("No File Given")



