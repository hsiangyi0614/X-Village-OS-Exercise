import numpy as np
import threading
import multiprocessing
import time
s=10#矩陣size
###-*Numpy處理兩矩陣相乘-*###
def main():
    
    matA = np.random.randint(10, size = (s, s))
    matB = np.random.randint(10, size = (s, s)) 
    #result = np.zeros((matA.shape[0], matB.shape[1]))
    start_time = time.time()
    normal=np.matmul(matA, matB)
    end_time =time.time()
    print('Normal time =', end_time - start_time)
    return matA,matB
    # Generate random matrix and result matrix
    
# def thread_func(matA_row, matB):
   
#     for row in range(0, matA.shape[0]):
#         result[row] = np.matmul(matA[row], matB)

# def thread_main(matA,matB):
#     thread_num = s
#     threads=[]
#     result=[]
#      # Assign job to threads
#     start_time = time.time()
#     for i in range(thread_num):
#         # Pass argument to function with tuple
#         thread = threading.Thread(target = thread_func,args=(matA[i],matB))
#         threads.append(thread)

#     # run all threads
#     for thread in threads:
#         thread.start()

#     # Wait for threads finish
#     for thread in threads:
#         thread.join()
#     end_time = time.time()
#     print('Tread time =', end_time - start_time)
    

if __name__=='__main__':
    matA,matB = main()
    # thread_main(matA,matB)
    