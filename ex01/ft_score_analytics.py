import sys

# TODO Process the command-line arguments
# TODO Handle the various erroneous cases (no arguments, non-numeric values) 
# with appropriate messages
# TODO Create a new list to store and organize the scores
# TODO Calculate some basic stats that would make any game player happy 
# (number, total, average, max, min, and range)
# TODO Make the output look cool enough to impress your gaming buddies 
# (you can mimic the example again)
# TODO If both valid and invalid inputs are provided via the command line, discard 
# the invalid ones and proceed with the remaining valid inputs unless none remain.

def main() -> None:
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {score}")
    print(f"Average score: {score}")
    print(f"High score: {score}")
    print(f"Low score: {score}")
    print(f"Score range: {score}")


if __name__ == "__main__":
    main()
