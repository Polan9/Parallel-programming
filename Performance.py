from joblib import Parallel, delayed
import time
from list_comprehension_sqrt import list_sqrt
from factorial import factorial

def Pom():
    for i in range(2,1000):
        start = time.time()
        print(factorial(i))
        end = time.time()
        time_taken = end - start
        print(f"The duration of calculations: {time_taken:.3f}s")

def performance(func, n_jobs_list,range1, range2, n1, n2=None, n3=None ):
    for i in range(len(n_jobs_list)):

        start = time.time()
        for _ in range(range1,range2):
            if n2 == None:
                a1 = Parallel(n_jobs=n_jobs_list[i])(delayed(func)(n1) for _ in range(n1))
            elif n2 is not None and n3 == None:
                a1 = Parallel(n_jobs=n_jobs_list[i])(delayed(func)(n1,n2 ) for _ in range(n1,n2))
            else:
                a1 = Parallel(n_jobs=n_jobs_list[i])(delayed(func)(n1,n2,n3) for _ in range(n1,n2,n3))

        end = time.time()
        time_taken = end - start
        print(f"The duration of calculations for n_jobs and for {func.__name__}= {n_jobs_list[i]}: {time_taken:.3f}s")

njobs_list = [2,5,10,15,25]


performance(list_sqrt, njobs_list, 0,1000,1,50)

performance(factorial, njobs_list, 0,1000,5)



