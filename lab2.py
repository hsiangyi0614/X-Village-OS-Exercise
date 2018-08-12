import threading
import queue
import os

buffer_size = 5

lock = threading.Lock()
queue = queue.Queue(buffer_size)
file_count = 0

def producer(top_dir, queue_buffer):
    lsdir=os.listdir(top_dir)
    queue_buffer.put(top_dir,block=True,timeout=10)
    for i in lsdir:
        newpath=os.path.join(top_dir,i)
        if os.path.isdir(newpath):
            producer(newpath,queue_buffer)
    return

def consumer(queue_buffer):
    lock.acquire()
    global file_count
    while not queue_buffer.empty():
        path=queue_buffer.get()
        lsdir=os.listdir(path)
        for i in lsdir:
            newpath=os.path.join(path,i)
            if os.path.isfile(newpath):
                file_count+=1
    lock.release()

def main():
    producer_thread = threading.Thread(target = producer, args = ('./Lab2', queue))
    global file_count
    consumer_count = 20
    consumers = []
    #producer_thread.start()
    
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    #input()
    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()
    print(file_count, 'files found.')
    
if __name__ == "__main__":
    main()