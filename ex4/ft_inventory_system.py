import sys


def parse():
    result: dict = {}
    for i in sys.argv:
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
        value: list = i.split(":")

        try:
            int(value[1])
        except Exception as e:
            print(f"Quantity error for ’{value[0]}’:")
        result[value[0]] = value[1]


if __name__ == "__main__":
    parse()
