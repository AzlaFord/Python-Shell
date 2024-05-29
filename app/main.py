import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_comands = input().strip()

        if user_comands == 'exit 0':
            sys.exit(0)
        
        elif user_comands.startswith('echo '):
            echo_text = user_comands[5:]
            print(echo_text)
        
        else:
            print(f"{user_comands}: command not found")

if __name__ == "__main__":
    main()
