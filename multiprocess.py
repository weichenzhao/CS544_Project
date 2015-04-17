"""
    test for multi-core usage
"""
def work(foo):
    count = 0
    while count < 100000000:
        count += 1

from multiprocessing import Pool

pool = Pool()
pool.map(work, range(10))
pool.close()
pool.join()
