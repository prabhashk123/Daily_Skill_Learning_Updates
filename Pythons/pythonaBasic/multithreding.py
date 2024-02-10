# part of operating system.
# library/module use threading
import threading
import time
# for deep and lunch parallel use concurrent.futures module threding use  I/O-bound tasks,
from concurrent.futures import ThreadPoolExecutor 

def function(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    # if return thane get return value by map
    return seconds
# for future make main func
def main():
    time1=time.perf_counter()
    # # Normal code  function without threading run by 4s thane 2s than 1s take time diferent not start one time run by wating
    # function(4)
    # function(2)
    # function(1)
    # time2=time.perf_counter()
    # print(time2-time1)
        
    #  same code By use threading basic
    t1=threading.Thread(target=function,args=[4])
    t2=threading.Thread(target=function,args=[2])
    t3=threading.Thread(target=function,args=[1])
    t1.start()
    t2.start()
    t3.start()
    # for end one by one use join
    t1.join()
    t2.join()
    t3.join()

    # calculate time
    time2=time.perf_counter()
    print(time2-time1)

# for advance threding
def poolDemo():
    # ThreadPoolExecutor is used to shedule lot of tasks in bulk.
    # with ThreadPoolExecutor(max_workers=1) as executor:
    with ThreadPoolExecutor() as executor:
        """Method-1"""
        # future = executor.submit(function,3)
        # future = executor.submit(function,2)
        # future = executor.submit(function,5)
        # print(future.result())
        # print(future.result())
        # print(future.result())
        """Method-2"""
        # result set parallel by download 50 urls at one time 
        lst=[3,5,1,2] # url1,url2..,future1,future2
        results=executor.map(function,lst) #iterate data
        for result in results:
            print(result)

poolDemo()
