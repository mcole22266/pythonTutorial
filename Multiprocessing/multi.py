import multiprocessing as mp
from time import time 

miniList = list(range(1000, 3000))
bigList = [miniList for _ in range(25)]

miniList = list(range(1000, 5000))
bigList = [miniList for _ in range(25)] 

def exponentiate(aList):
    print('Exponentiating a list')
    newList = [num**num for num in aList]
    print('Completed exponentiation')
    return newList 

if __name__ == "__main__":
    maxCPU = mp.cpu_count()
    numCPU = input('How many workers would you like to use? (input `max` to use all available workers).  ')
    if numCPU.strip().lower() == 'max':
        numCPU = maxCPU
    else:
        numCPU = int(numCPU)
        if numCPU > maxCPU:
            numCPU = maxCPU 


    workers = mp.Pool(numCPU)
    start = time()
    newList = workers.map(exponentiate, bigList)
    end = time()
    
    print()
    print('Done')
    print()
    print(f'It took {end-start} seconds for {numCPU} cpus to complete this task.')
