import sys
import os


class Research:
    def __init__(self, file_name):
        if len(sys.argv) == 2:
            self.file_name = file_name
        else:
            raise Exception("TypeError: Too many Arguments")

    def file_reader(self, has_header=True):
        try:
            with open(self.file_name, "r") as f:
                lines = f.read().strip().split("\n")
                if has_header:
                    lines = lines[1:]
                data = [list(map(int, line.split(","))) for line in lines]
                return data
        except Exception as e:
            raise Exception(f"File reading error: {e}")

    class Calculations:
        @staticmethod
        def counts(res_lst):
            heads = 0
            tails = 0
            for lst in res_lst:
                if lst[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction


if __name__ == "__main__":
    try:
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)

        calculations = Research.Calculations()
        heads, tails = calculations.counts(data)
        print(heads, tails)

        head_fraction, tail_fraction = calculations.fractions(heads, tails)
        print(head_fraction, tail_fraction)

    except Exception as e:
        print(e)
