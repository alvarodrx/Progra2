# from multiprocessing import Process
# import time
#
# def f(name, num):
#     print('hello', name, num)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     h = time.time()
#     for i in range(20):
#         p = Process(target=f, args=('bob',i,))
#         p.start()
#         p.join()
#     print("Duración:",time.time()-h)}

#
# import matplotlib.pyplot as plt
# from functools import partial
# import multiprocessing
#
#
# def mandelbrotCalcRow(yPos, h, w, max_iteration=1000):
#     y0 = yPos * (2 / float(h)) - 1  # rescale to -1 to 1
#     row = []
#     for xPos in range(w):
#         x0 = xPos * (3.5 / float(w)) - 2.5  # rescale to -2.5 to 1
#         iteration, z = 0, 0 + 0j
#         c = complex(x0, y0)
#         while abs(z) < 2 and iteration < max_iteration:
#             z = z ** 2 + c
#             iteration += 1
#         row.append(iteration)
#     return row
#
#
# def mandelbrotCalcSet(h, w, max_iteration=1000):
#     # make a helper function that better supports pool.map by using only 1 var
#     # This is necessary since the version
#     partialCalcRow = partial(mandelbrotCalcRow, h=h, w=w, max_iteration=max_iteration)
#
#     pool = multiprocessing.Pool()  # creates a pool of process, controls worksers
#     # the pool.map only accepts one iterable, so use the partial function
#     # so that we only need to deal with one variable.
#     mandelImg = pool.map(partialCalcRow, range(h))  # make our results with a map call
#     pool.close()  # we are not adding any more processes
#     pool.join()  # tell it to wait until all threads are done before going on
#
#     return mandelImg
#
# ''' Algoritmo normal
# def mandelbrotCalcSet(h, w, max_iteration = 1000):
#     partialCalcRow = partial(mandelbrotCalcRow, h=h, w=w, max_iteration = max_iteration)
#     mandelImg = map(partialCalcRow, xrange(h))
#     return mandelImg'''
#
#
# if __name__=='__main__':
#     mandelImg = mandelbrotCalcSet(1000, 1000, 500)
#     plt.imshow(mandelImg)
#     plt.savefig('mandelimg0.png')

# import multiprocessing
# import time
#
# class prueba:
#     muestra = 0
#     def __init__(self, maxPool):
#         self.pool = multiprocessing.Pool(1)
#         m = multiprocessing.Manager()
#         self.queue = m.Queue()
#         self.Max =maxPool
#
#     def subprocess(self, proces, iter):
#         for i in range(iter):
#             print("Running", proces, self.muestra)
#             self.muestra += 1
#             time.sleep(1)
#         print("Subprocess",proces," Completed")
#
#     def subprocess2(self):
#         for i in range(self.Max):
#             print("Running2",self.muestra)
#             self.muestra += 1
#             time.sleep(1)
#         print("Subprocess Completed")
#
#     def start(self):
#         self.pool = multiprocessing.Pool(self.Max)
#         for i in range(self.Max):
#             self.pool.apply_async(func=self.subprocess,args=(i,i*2))
#             print("Subprocess",i," has been started")
#         self.pool.close()
#         self.pool.join()
#
#     def __getstate__(self):
#         self_dict = self.__dict__.copy()
#         del self_dict['pool']
#         return self_dict
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#
# if __name__ == '__main__':
#
#     p = prueba(10)
#     h = time.time()
#     p.start()
#     print("Duración:",time.time()-h)

# import multiprocessing
#
# def worker(procnum, return_dict):
#     '''worker function'''
#     print(str(procnum) + ' represent!')
#     return_dict[procnum] = procnum
#
#
# if __name__ == '__main__':
#     manager = multiprocessing.Manager()
#     return_dict = manager.dict()
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,return_dict))
#         jobs.append(p)
#         p.start()
#
#     for proc in jobs:
#         proc.join()
#     print (return_dict.values())

# import multiprocessing
# import threading
# from time import sleep
#
# def run(i, conn):
#     try:
#         f(i)
#     except CustomException as e:
#         conn.send(e)
#
# def f(i):
#    print(i, ' called')
#    sleep(i)
#    if i == 11:
#        raise CustomException
#    print(i, ' done')
#
# class CustomException(Exception):
#     pass
#
# class ProcessManager(object):
#     def __init__(self):
#         self.processes = []
#         self._threads = []
#         self._lock = threading.Lock()
#
#     def terminate_all(self):
#         with self._lock:
#             for p in self.processes:
#                 if p.is_alive():
#                     print("Terminating %s" % p)
#                     p.terminate()
#
#     def launch_proc(self, func, args=(), kwargs= {}):
#         t = threading.Thread(target=self._proc_thread_runner,
#                              args=(func, args, kwargs))
#         self._threads.append(t)
#         t.start()
#
#     def _proc_thread_runner(self, func, args, kwargs):
#         parent_conn, child_conn = multiprocessing.Pipe()
#         args = args + tuple([child_conn])
#         p = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
#         self.processes.append(p)
#         p.start()
#         while p.exitcode is None:
#             p.join()
#         if parent_conn.poll():
#             obj = parent_conn.recv()
#             if isinstance(obj, CustomException):
#                 self.terminate_all()
#
#     def wait(self):
#         for t in self._threads:
#             t.join()
#
# if __name__ == '__main__':
#     proc_manager = ProcessManager()
#     for i in range(0, 20):
#         proc_manager.launch_proc(run, (i,))
#     proc_manager.wait()

import time
import numpy as np
import multiprocessing as mp
import time
import sys
import os
import psutil
import signal

pid_array = []

def f(i):
    np.random.seed(int(time.time()+i))

    time.sleep(3)
    res=np.random.rand()
    current_process = os.getpid()
    print( "From i = ",i, "       res = ",res, " with process ID (pid) = ", current_process)
    if res>0.7:
        print("find it")
        # solution: use the parent child connection between processes
        parent = psutil.Process(main_process)
        children = parent.children(recursive=True)
        print("asd")
        for process in children:
            if not (process.pid == current_process):
                print("Process: ",current_process,  " killed process: ", process.pid)
                process.send_signal(signal.SIGTERM)
    else:
        time.sleep(20)

main_process = os.getpid()
if __name__=='__main__':
    #main_process = os.getpid()
    num_workers=mp.cpu_count()
    pool=mp.Pool(num_workers)

    print("Main process: ", main_process)
    for i in range(num_workers):
        p=mp.Process(target=f,args=(i,))
        p.start()
