class Research:
    def file_reader(self):
        try:
            file = "../ex00/data.csv"
            with open(file, "r") as f:
                return f.read().strip()
        except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    var = Research()
    print(var.file_reader())
