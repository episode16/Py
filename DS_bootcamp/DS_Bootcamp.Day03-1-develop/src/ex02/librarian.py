import os
import sys


def check_env(expected_env):
    current_env = os.environ.get("VIRTUAL_ENV")
    if not current_env or os.path.basename(current_env) != expected_env:
        raise EnvironmentError(
            f"Script must be run inside the '{expected_env}' virtual environment. Current: {current_env}"
        )


def install():
    os.system("pip3 install beautifulsoup4 pytest")


def save_installed_libraries():
    os.system("pip3 freeze")
    os.system("pip3 freeze > requirements.txt")


if __name__ == "__main__":
    try:
        expected_env = "morrowto"
        check_env(expected_env)
        install()
        save_installed_libraries()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
