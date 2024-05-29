import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        if not user_comands:
            continue
        
        if user_comands := input().strip():

            if user_comands == 'exit 0':
                sys.exit(0)
            elif user_comands.startswith('echo '):
                # Extrage textul după 'echo ' și îl afișează
                echo_text = user_comands[5:]
                print(echo_text)  
            else:
                print(f"{user_comands}: command not found")




if __name__ == "__main__":
    main()
