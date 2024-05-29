import sys


def main():


    sys.stdout.write("$ ")
    sys.stdout.flush()
    comand = input()

    print(f"{comand}: command not found")


if __name__ == "__main__":
    main()
