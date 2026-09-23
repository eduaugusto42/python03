#!/usr/bin/env python3

from random import randint


ACHIEVEMENTS = (
            'Boss Slayer',
            'Collector Supreme',
            'Crafting Genius',
            'First Steps',
            'Hidden Path Finder',
            'Master Explorer',
            'Untouchable',
            'Sharp Mind',
            'Speed Runner',
            'Strategist',
            'Survivor',
            'Treasure Hunter',
            'Unstoppable',
            'World Savior'
            )


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievement(randint(1, 14))
    print(f"Player Alice: {alice}")
    bob = gen_player_achievement(randint(1, 14))
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievement(randint(1, 14))
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievement(randint(1, 14))
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Alice is missing: {set(ACHIEVEMENTS).difference(alice)}")
    print(f"Bob is missing: {set(ACHIEVEMENTS).difference(bob)}")
    print(f"Charlie is missing: {set(ACHIEVEMENTS).difference(charlie)}")
    print(f"Dylan is missing: {set(ACHIEVEMENTS).difference(dylan)}")


def gen_player_achievement(amount: int) -> set[str]:
    player_achievements: set[str] = set()

    while len(player_achievements) < amount:
        player_achievements.add(
                ACHIEVEMENTS[randint(0, len(ACHIEVEMENTS) - 1)]
                )
    return player_achievements


if __name__ == "__main__":
    main()
