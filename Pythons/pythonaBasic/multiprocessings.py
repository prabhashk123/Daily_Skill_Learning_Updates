# part of operating system.
# use for multiple cpu bond then use multiprocessing (computer processing unit)
# use paralle different-different computer/cpu
# for parallel downloading example here
# it is python module that provide simple way to running multiple process in parallel.
# if __name__ == '__main__':
#     freeze_support()  # Add this line for executables
#     # Rest of your multiprocessing code
import multiprocessing 
# from multiprocessing import Process
# from multiprocessing import Process
import requests

def downloadFile(url,name):
    print(f"Start downloading{name}")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"finished downloading{name}")
if __name__ == '__main__':
    url="https://picsum.photos/200"
    # for multiprocessing
    pros=[]
# use underscore here for throw because i dont need i print() so use.
# for _ in range(5):

    for i in range(5):
        # downloadFile(url,i)
        # use multiprocessing
        p=multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()


