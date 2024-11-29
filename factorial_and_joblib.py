

from factorial import factorial
from joblib import delayed, Parallel
import time

njobs_list = [2,5,10,15,25]

for i in range(len(njobs_list)):
    start = time.time()
    a1 = Parallel(n_jobs=njobs_list[i])(delayed(factorial)(i) for i in range(3,10))
    end = time.time()
    time_taken = end - start
    print(f"czas trwania obliczen dla njobs = {njobs_list[i]}: {time_taken:.3f}")



test = factorial(5)
print(test)
