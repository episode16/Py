import timeit
import sys
from functools import reduce


def first_method(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i * i
    return sum


def fifth_method_reduce(num):
    return reduce(lambda sum, i: sum + i * i, range(1, num + 1))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise Exception(
                "There must be three arguments: <func_name> <num_of_calls> <number>"
            )
        else:
            number = int(sys.argv[3])
            # Замена globals() на лямбда-функции
            if sys.argv[1] == "loop":
                first_method_time = timeit.timeit(
                    lambda: first_method(number), number=int(sys.argv[2])
                )
                print(first_method_time)
            elif sys.argv[1] == "reduce":
                fifth_method_time = timeit.timeit(
                    lambda: fifth_method_reduce(number), number=int(sys.argv[2])
                )
                print(fifth_method_time)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
