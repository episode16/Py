import sys
import resource


def open_file(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line


def get_resource():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    memory_usage = usage.ru_maxrss / 1024 / 1024  # Конвертируем в ГБ
    time_usage = usage.ru_utime + usage.ru_stime  # Пользовательское + системное время
    print(f"Peak Memory Usage = {memory_usage:.3f} GB")
    print(f"User Mode Time + System Mode Time = {time_usage:.3f} s")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("There must be three arguments: <name.py> <name.csv>")
        else:
            lines = open_file(sys.argv[1])
            for line in lines:
                pass
            get_resource()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
