import random
import typing


# Generator [yield value,send type , return type ]
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions: list[str] = [
        "run",
        "sleep",
        "grab",
        "climb",
        "swim",
        "release",
        "move",
    ]

    for i in range(1000):
        player = random.sample(players, random.randint(1, 1))
        action = random.sample(actions, random.randint(1, 1))

        yield (player[0], action[0])


def build_event() -> typing.Generator[list[tuple[str, str]], None, None]:
    gen = gen_event()
    built_list: list[tuple[str, str]] = []
    for i in range(10):
        built_list.append(next(gen))

    print(f"Built list of 10 events: {built_list}")

    n = 10
    while n:
        choose = random.sample(built_list, random.randint(1, 1))
        print(f"Got event from list: {choose[0]}")
        built_list.remove(choose[0])
        yield built_list
        n -= 1


if __name__ == "__main__":

    counter: int = 0
    for i in gen_event():
        print(f"Event {counter}: Player {str(i[0])} action {str(i[1])}")
        counter += 1
    gen: typing.Generator[list[tuple[str, str]], None, None] = build_event()
    for _ in range(10):
        print(f"Remains in list {next(gen)}")
