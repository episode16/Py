import os
from random import randint


class Research:
    def __init__(self, file_name):
        self.file_name = file_name

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
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = len(self.data) - heads
            return heads, tails

        def fractions(self):
            heads, tails = self.counts()
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction

    class Analytics(Calculations):
        def predict_random(self, num_of_predictions):
            predictions = []
            for _ in range(num_of_predictions):
                head = randint(0, 1)
                predictions.append([head, 1 - head])
            return predictions

        def predict_last(self):
            return self.data[-1]

        @staticmethod
        def save_file(data, filename, extension="txt"):
            if not isinstance(data, str):
                data = str(data)
            with open(f"{filename}.{extension}", "w") as f:
                f.write(data)
