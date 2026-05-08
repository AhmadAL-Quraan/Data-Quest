import random


def gen_player_achievements() -> set[str]:
    achiv = [
        "Crafting Genius",
        "World Savior",
        "MasterExplorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Unstoppable",
        "Collector Supreme",
        "Untouchable",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "MasterExplorer",
        "Treasure Hunter",
        "First Steps",
        "Untouchable",
        "Sharp Mind",
        "Strategist",
        "Speed Runner",
        "Unstoppable",
        "Untouchable",
        "Boss Slayer",
    ]
    # random.sample: Return a list of unique
    return set(random.sample(achiv, random.randint(1, len(achiv))))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player1: tuple[str, set[str]] = ("Alice", gen_player_achievements())
    player2: tuple[str, set[str]] = ("Bob", gen_player_achievements())
    player3: tuple[str, set[str]] = ("Dylan", gen_player_achievements())
    player4: tuple[str, set[str]] = ("Charlie", gen_player_achievements())

    diff1 = player1[1] - (player2[1] | player3[1] | player4[1])
    union: set[str] = set()
    # Union: combine two or more sets into a new one
    # intersection: similarity between two or more set
    # diff : elements exists in one set but not in the other
    # | -> Union, & -> intersection,
    # ^ ->symmetric difference, - difference (A - B)
    for i in [player1, player2, player3, player4]:
        union |= i[1]

        print(f"Player {i[0]}: {i[1]}")
    # If set is empty it reutnr set() -> to make it unique compares to dict
    print(f"\nAll distinct achievements: {union}")
    print(f"\nCommon achievements: \
{(player1[1] & player2[1] & player3[1] & player4[1])}\n")

    print((player2[1] | player3[1] | player4[1]))
    diff1 = player2[1] - (player1[1] | player3[1] | player4[1])
    diff2 = player3[1] - (player2[1] | player1[1] | player4[1])
    diff3 = player4[1] - (player2[1] | player3[1] | player1[1])
    print(f"Only Alice has: \
{diff1}\n" f"Only Bob has: \
{diff1}\n" f"Only Dylan has:\
{diff2}\n" f"Only Charlie has: \
{diff3}\n")
    print(f"Alice is missing: {union - player1[1]}")
    print(f"Bob is missing: {union - player2[1]}")
    print(f"Charlie is missing: {union - player4[1]}")
    print(f"Dylan is missing: {union - player3[1]}")
