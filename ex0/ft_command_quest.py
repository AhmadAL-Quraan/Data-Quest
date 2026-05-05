import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total_arg: int = len(sys.argv)
    if total_arg == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments\
 received: {total_arg}")
        for i in range(len(sys.argv)):
            if i != 0:
                print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total_arg}")
