import sys


def parse() -> None:
    result: dict[str, int] = {}
    j: int = 0
    for j in range(1, len(sys.argv)):
        i = sys.argv[j]
        # check if string has :
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        key_val: list[str] = i.split(":")
        # Check if value is int
        try:
            int(key_val[1])
        except Exception as e:
            print(f"Quantity error for ’{key_val[0]}’: {e}")
            continue
        # Check Redundant
        value: int = result.get(key_val[0], -1)
        if value == -1:
            result[key_val[0]] = int(key_val[1])
        else:
            print(f"Redundant item ’{key_val[0]}’ - discarding")

    print(f"Got inventory: {result}")
    Item_list = list(result.keys())
    print(f"Item list: {Item_list}")
    summation = sum(result.values())
    print(f"Total quantity of the {len(Item_list)} items: {summation}")
    for i in Item_list:
        print(
            f"Item {i} represents {(result.get(i, -1) / summation) * 100:.1f}%"
        )

    save_max: str = ""
    save_min: str = ""
    value_max: int = 0
    value_min: int = 99999999
    for key, value in result.items():
        if value > value_max:
            value_max = value
            save_max = key
        if value < value_min:
            value_min = value
            save_min = key

    if len(sys.argv) != 1:
        print(f"Item most abundant: {save_max} with quantity {value_max}")
        print(f"Item least abundant: {save_min} with quantity {value_min}")

    result["magic_item"] = 1  # Or result.update({"magic_item":1})

    print(f"Updated inventory: {result}")


if __name__ == "__main__":
    parse()
