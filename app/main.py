import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_comands = input()
        if user_comands := input().strip():

            if user_comands == 'exit 0':
                sys.exit(0)
                
            else:
                print(f"{user_comands}: command not found")




if __name__ == "__main__":
    main()
