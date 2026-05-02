import math


# Tuples are : ordered, immutable, allow duplicates, heterogeneous
def get_player_pos():
    clean_data: tuple[float, float, float] = (0.0, 0.0, 0.0)
    data: str = ""
    invalid: bool = True
    user_input = ""
    while invalid:
        clean_data = (0.0, 0.0, 0.0)
        user_input = input(
            "Enter new coordinates as floats in format ’x,y,z’: "
        ).split(",")
        invalid = False
        for i in user_input:
            try:
                data = i
                float(data)

            except ValueError as e:
                print(f"Error on parameter '{data}': {e}")
                invalid = True

        if len(user_input) > 3:
            print("3 numbers only allowed")
            invalid = True
    clean_data = (
        float(user_input[0]),
        float(user_input[1]),
        float(user_input[2]),
    )

    x: float = clean_data[0]
    y: float = clean_data[1]
    z: float = clean_data[2]
    print(f"Got first tuple: {clean_data}")
    print(f"It includes: X={x}, Y={y}, Z={z}")

    print(f"Distance to center: { math.sqrt((x**2 + y**2 + z**2)):.6f}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===\n")
    print("Get a first set of coordinates")
    get_player_pos()
    print("Get a second set of coordinates")
    get_player_pos()
