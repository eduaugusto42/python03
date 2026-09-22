#!/usr/bin/env python3

import math

def main() -> None:
    center = (0.0, 0.0, 0.0)

    print("=== Game Coordinate System ===")
    print()
    print("Get first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    print(
            "Distance to center: "
            f"{round(calculate_distance(p1, center), 4)}"
            )
    print()
    print("Get second set of coordinates")
    p2 = get_player_pos()
    print(
            "Distance between the 2 sets of coordinates: "
            f"{round(calculate_distance(p1, p2), 4)}"
            )

def get_player_pos() -> tuple[float, float, float]:
    while True:
        pos = ()

        coordinates = input(
                "Enter new coordinates as floats in format 'x, y, z': "
                )
        values = coordinates.split(",")
        if len(values) != 3:
            print("Invalid syntax")
            continue
        for value in values:
            try:
                pos = pos + (float(value),)
            except ValueError:
                print(
                        f"Error on parameter '{value}': "
                        f"could not convert string to float: '{value}'"
                        )
        if len(pos) == 3:
            break
    return pos

def calculate_distance(
        p1: tuple[float, float, float], 
        p2: tuple[float, float, float]
        ) -> float:
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

if __name__ == "__main__":
    main()
