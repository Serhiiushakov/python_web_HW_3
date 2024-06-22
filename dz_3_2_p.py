import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def factorize(*numbers):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        result = list(executor.map(factors, numbers))
    return result

if __name__ == "__main__":
    # Перевірка роботи та вимірювання часу виконання паралельної версії
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()

    print(f"Паралельна версія виконана за {end_time - start_time:.4f} секунд")
    print(a)
    print(b)
    print(c)
    print(d)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

# РЕЗУЛЬТАТ:
# Паралельна версія виконана за 1.7701 секунд
# [1, 2, 4, 8, 16, 32, 64, 128]
# [1, 3, 5, 15, 17, 51, 85, 255]
# [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
