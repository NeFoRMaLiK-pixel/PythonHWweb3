import time
from multiprocessing import Pool, cpu_count

def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize_sync(*numbers):
    return [factors(number) for number in numbers]

def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factors, numbers)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    sync_result = factorize_sync(*numbers)
    sync_time = time.time() - start_time
    print(f"Синхронная версия: {sync_result}")
    print(f"Время выполнения (синхронно): {sync_time:.2f} секунд")

    start_time = time.time()
    parallel_result = factorize_parallel(*numbers)
    parallel_time = time.time() - start_time
    print(f"Параллельная версия: {parallel_result}")
    print(f"Время выполнения (параллельно): {parallel_time:.2f} секунд")

    assert sync_result == parallel_result, "Результаты синхронной и параллельной версии не совпадают!"