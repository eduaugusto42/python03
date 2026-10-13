import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print_arguments()
    print(f"Total arguments: {len(sys.argv)}")


def print_arguments() -> None:
    length: int = len(sys.argv)
    i: int = 1

    if length == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1


if __name__ == "__main__":
    main()
