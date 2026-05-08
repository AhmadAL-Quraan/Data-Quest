import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    names: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    print(f"Initial list of players: {names}")
    names_capital: list[str] = [x.capitalize() for x in names]
    print(f"New list with all names capitalized: {names_capital}")
    print(f"New list of\
 capitalized names only: {[x for x in names if x == x.capitalize()]}\n")

    dic: dict[str, int] = {x: random.randint(1, 1000) for x in names_capital}

    print(f"Score dict: {dic}")
    average: float = sum(value for key, value in dic.items()) / len(dic)
    print(f"Score average is {average:.2f}")

    new_dic: dict[str, int] = {
        key: value for key, value in dic.items() if value > average
    }
    print(f"High scores: {new_dic}")
