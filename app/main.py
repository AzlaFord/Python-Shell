import sys

def main():
    valid_comands = {}

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_comands = input().strip().split()  # Citește și împarte comanda în cuvinte
        
        if len(user_comands) > 0 and user_comands[0] == "exit":
            if len(user_comands) == 2 and user_comands[1] == "0":
                print("Exiting the program with status 0. Goodbye!")
                sys.exit(0)  # Termină programul cu codul de stare 0
            else:
                print(f"{user_comands}: invalid exit command")
        
        if user_comands[0] not in valid_comands:
            print(f"{user_comands[0]}: command not found")

if __name__ == "__main__":
    main()
