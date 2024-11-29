from list_comprehension_sqrt import list_sqrt
import time
from joblib import delayed, Parallel

njobs_list = [2,5,10,15,25]
for i in range(len(njobs_list)):
    start = time.time()
    a1 = Parallel(n_jobs=njobs_list[i])(delayed(list_sqrt)(0,200) for _ in range(njobs_list[i]))
    end = time.time()
    time_taken = end - start
    print(f"The duration of calculations for n_jobs = {njobs_list[i]}: {time_taken:.3f}s")


