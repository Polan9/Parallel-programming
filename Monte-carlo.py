from joblib import Parallel, delayed
import random
def MonteCarlo(n):
    n_traf = 0
    for i in range(n):
        x, y = (random.uniform(-1,1), random.uniform(-1,1))
        print(x,y)
        if x**2 + y**2 <= 1:
            n_traf+=1
    pi = 4 * (n_traf / n)
    print(pi)



a1 = Parallel(n_jobs=15)(delayed(MonteCarlo)(100000) for i in range(5))

