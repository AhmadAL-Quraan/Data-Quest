import sys

if __name__ == "__main__":
    scores = []
    val = ""
    for i in range(1, len(sys.argv)):
        try:
            val = sys.argv[i]
            scores.append(int(val))
        except ValueError:
            print(f"Invalid parameter: {val}")

    if len(scores) == 0:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]} <score1><score2> ..."
        )
        exit(0)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(sys.argv)- 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/ len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
