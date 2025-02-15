import sys
import os


class Research:
    def __init__(self, file_name):
        if len(sys.argv) == 2:
            self.file_name = file_name
        else:
            raise Exception("TypeError: Too many Arguments")

    def file_reader(self):
        try:
            with open(self.file_name, "r") as f:
                return f.read().strip()
        except Exception as e:
            print(f"{e}")
            return None


if __name__ == "__main__":
    try:
        var = Research(sys.argv[1])
        print(var.file_reader())
    except Exception as e:
        print(f"{e}")
