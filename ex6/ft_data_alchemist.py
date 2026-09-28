#!/usr/bin/env python3

import random

def main() -> None:
    players = [
            'Alice',
            'bob',
            'Charlie',
            'dylan',
            'Emma',
            'Gregory',
            'john',
            'kevin',
            'Liam'
            ]
    players_title = [player.title() for player in players]
    title_only = [player for player in players if player == player.title()]
    scores = {player: random.randint(0, 999) for player in players_title}
    average = round(sum(scores.values()) / len(scores), 2)
    high_scores = {
            player: scores[player] for player in scores if scores[player] > average
            }

    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_title}")
    print(f"New list of capitalized names only: {title_only}")
    print()
    print(f"Score dict: {scores}")
    print(f"Score average is {average}")
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()
