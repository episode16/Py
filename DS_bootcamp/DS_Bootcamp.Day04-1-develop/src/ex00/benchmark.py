from timeit import timeit


def first_method(emails):
    res = []
    for email in emails:
        if "@gmail.com" in email:
            res.append(email)
    return res


def second_method(emails):
    return [email for email in emails if "@gmail.com" in email]


if __name__ == "__main__":
    try:
        emails = [
            "john@gmail.com",
            "james@gmail.com",
            "alice@yahoo.com",
            "anna@live.com",
            "philipp@gmail.com",
        ] * 5

        first_method_time = timeit(lambda: first_method(emails), number=90000000)
        second_method_time = timeit(lambda: second_method(emails), number=90000000)

        if second_method_time <= first_method_time:
            print("it is better to use a list comprehension")
        else:
            print("it is better to use a loop")

        times = sorted([first_method_time, second_method_time])
        print(f"{times[0]:.6f} vs {times[1]:.6f}")
    except Exception as e:
        print(f"Error: {e}")
