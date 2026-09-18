import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = process_scores()
    if len(scores) == 0:
        print(
                "No scores provided. "
                f"Usage: {sys.argv[0]} <score1> <score2> ..."
                )
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def process_scores() -> list[int]:
    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


if __name__ == "__main__":
    main()
