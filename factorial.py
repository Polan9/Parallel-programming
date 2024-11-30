from joblib import Parallel, delayed
import time
from list_comprehension_sqrt import list_sqrt

def factorial(n):
    list_of_numbers = [i for i in range(n + 1)]
    result = []
    for i in range(len(list_of_numbers)):
        list_of_numbers.pop(0)
        if len(list_of_numbers) > i + 1:
            tmp = list_of_numbers[i] * list_of_numbers[i + 1]
            list_of_numbers[i + 1] = tmp
            list_of_numbers.append(tmp)
            result.append(tmp)
    return max(result)

