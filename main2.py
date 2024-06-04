from insertion_sort import insertion_sort
from merge_sort import merge_sort
from numpy.random import randint
import pandas as pd
import multiprocessing, time

def sort(alg_name, alg, A, n, result_queue):
    start_time = time.time()
    print(f'\nInício {alg_name}, {n}. --------------')
    alg(A.copy())
    end_time = time.time()
    total_time = end_time - start_time
    print(f'\nFim {alg_name}, {n}. {total_time}')
    result_queue.put((alg_name, n, total_time))


if __name__ == '__main__':
    ns = [1000, 10000, 100000, 1000000]
    As = {n: randint(0, 1000000000, n) for n in ns}
    algs = {
        'InsertionSort': insertion_sort,
        'MergeSort': merge_sort
    }
    results = []
    result_queue = multiprocessing.Queue()

    processos = []
    for n, A in As.items():
        for alg_name, alg in algs.items():
            p = multiprocessing.Process(target=sort, args=(alg_name, alg, A, n, result_queue))
            processos.append(p)

    for p in processos:
        p.start()

    for p in processos:
        p.join()

    while not result_queue.empty():
        results.append(result_queue.get())

    df = pd.DataFrame(results, columns=['Algoritmo', 'Tamanho', 'Tempo'])

    print(df)

    df.to_csv('Tempos.csv', index=False)