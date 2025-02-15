#!/usr/bin/env python3
import os


def print_current_venv():
    venv = os.environ["VIRTUAL_ENV"]
    print(f"Your current virtual env is {venv}")


if __name__ == "__main__":
    try:
        print_current_venv()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
