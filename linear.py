from insertion_sort import insertion_sort
from merge_sort import merge_sort
from datetime import datetime
from numpy.random import randint

def sort(alg_name, alg, A, n):
    start_time = datetime.now()
    print(f'\nInício {alg_name}, {n}. --------------')
    alg(A.copy())
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'\nFim {alg_name}, {n}. {total_time}')

if __name__ == '__main__':
    ns = [1000, 10000, 100000, 1000000]
    As = {n: randint(0, 1000000000, n) for n in ns}
    algs = {
        'InsertionSort': insertion_sort,
        'MergeSort': merge_sort
    }

    for n, A in As.items():
        for alg_name, alg in algs.items():
            sort(alg_name, alg, A, n)
    