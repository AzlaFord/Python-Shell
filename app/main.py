import sys


def main():



    
    valid_comands = {}

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_comands = input()
        if user_comands == 'exit':
            sys.exit()
            
        else:
            print(f"{user_comands}: command not found")




if __name__ == "__main__":
    main()
