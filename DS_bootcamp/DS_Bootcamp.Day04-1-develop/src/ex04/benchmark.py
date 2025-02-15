import timeit
import random
from collections import Counter


def count_numbers_manual(lst):
    counts = {i: 0 for i in range(101)}
    for num in lst:
        counts[num] += 1
    return counts


def top_10_manual(lst):
    counts = count_numbers_manual(lst)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:10]


def count_numbers_counter(lst):
    return dict(Counter(lst))


def top_10_counter(lst):
    return Counter(lst).most_common(10)


def time_manual(lst):
    return timeit.timeit(lambda: count_numbers_manual(lst), number=1)


def time_counter(lst):
    return timeit.timeit(lambda: count_numbers_counter(lst), number=1)


def time_top_manual(lst):
    return timeit.timeit(lambda: top_10_manual(lst), number=1)


def time_top_counter(lst):
    return timeit.timeit(lambda: top_10_counter(lst), number=1)


if __name__ == "__main__":
    random_list = [random.randint(0, 100) for _ in range(1000000)]
    print(f"my function: {time_manual(random_list)}")
    print(f"Counter: {time_counter(random_list)}")
    print(f"my top: {time_top_manual(random_list)}")
    print(f"Counter's top: {time_top_counter(random_list)}")
