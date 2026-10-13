#!/usr/bin/env python3
import random
import typing


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "use", "release"
]


def main() -> None:
    g: typing.Generator[tuple[str, str], None, None] = gen_event()
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")
    events: list[tuple[str, str]] = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    consume_ev: typing.Generator[tuple[str, str], None, None] = (
        consume_event(events)
    )
    for event in consume_ev:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        yield events.pop(random.randrange(len(events)))


if __name__ == "__main__":
    main()
