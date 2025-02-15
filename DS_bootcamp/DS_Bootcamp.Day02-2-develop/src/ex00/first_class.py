class Must_read:
    try:
        file = "data.csv"
        with open(file, "r") as f:
            print(f.read().strip())
    except Exception as e:
            print(f"{e}")


if __name__ == "__main__":
    var = Must_read()
