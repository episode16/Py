import timeit
import sys


def first_method(emails):
    res = []
    for email in emails:
        if "@gmail.com" in email:
            res.append(email)
    return res


def second_method(emails):
    return [email for email in emails if "@gmail.com" in email]


def third_method(emails):
    # return list(map(lambda email: email if "@gmail.com" in email else None, emails))
    return map(lambda email: email if "@gmail.com" in email else None, emails)


def fourth_method(emails):
    return filter(lambda email: "@gmail.com" in email, emails)


if __name__ == "__main__":

    try:
        emails = [
            "john@gmail.com",
            "james@gmail.com",
            "alice@yahoo.com",
            "anna@live.com",
            "philipp@gmail.com",
        ] * 5

        if len(sys.argv) != 3:
            raise Exception("There must be two arguments: <func_name> <num_of_calls>")

        method_map = {
            "loop": first_method,
            "list_comprehension": second_method,
            "map": third_method,
            "filter": fourth_method,
        }

        method_name = sys.argv[1]
        num_of_calls = int(sys.argv[2])

        if method_name not in method_map:
            raise Exception(f"Unknown method: {method_name}")

        method = method_map[method_name]

        time_taken = timeit.timeit(lambda: method(emails), number=num_of_calls)
        print(time_taken)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
