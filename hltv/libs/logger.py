from termcolor import colored


def error(x: str):
    print(f"{colored('[ERROR]', 'white', 'on_red')} {x}")


def warning(x: str):
    print(f"{colored('[WARNING]', 'white', 'on_yellow')} {x}")


def info(x: str):
    print(f"{colored('[INFO]', 'white', 'on_blue')} {x}")


def success(x: str):
    print(f"{colored('[SUCCESS]', 'white', 'on_green')} {x}")


def request(x: str):
    print(f"{colored('[REQUEST]', 'white', 'on_cyan')} {x}")
