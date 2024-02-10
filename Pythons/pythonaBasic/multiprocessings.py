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
import concurrent.futures

def downloadFile(url,name):
    print(f"Start downloading{name}")
    response=requests.get(url)
    open(f"file {name}.jpg","wb").write(response.content)
    print(f"finished downloading{name}")

if __name__ == '__main__':
    url="http://127.0.0.1:8000/product_imgs"
    # for multiprocessing
    pros=[]
# use underscore here for throw because i dont need i print() so use.
# for _ in range(5):
    
    # for i in range(5):
    #     # downloadFile(url,i)
    #     # use multiprocessing
    #     p=multiprocessing.Process(target=downloadFile,args=[url,i])
    #     p.start()
    #     pros.append(p)
    # for p in pros:
    #     p.join()
# for module con use for multiple then map data
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(60)]
        l2=[i for i in range(60)]
        results=executor.map(downloadFile,l1,l2)
        for r in results:
            print(r)


