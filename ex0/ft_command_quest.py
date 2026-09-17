import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print_arguments()
    print(f"Total arguments: {len(sys.argv)}")


def print_arguments() -> None:
    lenght = len(sys.argv)
    if lenght == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {lenght - 1}")
        for i in range(1, lenght):
            print(f"Argument {i}: {sys.argv[i]}")


if __name__ == "__main__":
    main()
