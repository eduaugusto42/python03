#!/usr/bin/env python3

from random import choice
from random import randrange
from typing import Generator


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
        "climb", "eat", "grab", "move", "run", "sleep", "swim"
        ]


def main() -> None:
    events: list[tuple[str, str]] = []
    g: Generator[tuple[str, str], None, None] = gen_event()

    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        player, action = next(g)
        print(f"Event {i}: Player {player} did action {action}")
    for _ in range(10):
        events = events + [next(g)]
    print(f"Build list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (choice(PLAYERS), choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        yield events.pop(randrange(len(events)))


if __name__ == "__main__":
    main()
