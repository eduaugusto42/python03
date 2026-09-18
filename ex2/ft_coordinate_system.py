import math

# Authorized: import math, math.sqrt(), input(), round(), print()

# TODO Get a first set of coordinates
# TODO Display the tuple then display each coordinate separately
# TODO Calculate the distance to the 3D center (0, 0, 0) (see below)
# TODO Get a new set of coordinates
# TODO Calculate the distance between the second and the first sets of coordinates

def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    print()
    print("Get second set of coordinates")
    p2 = get_player_pos()

# O quadrado da hipotenusa é meu pau que te lambusa

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


if __name__ == "__main__":
    main()
