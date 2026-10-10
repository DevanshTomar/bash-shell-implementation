from ast import match_case
import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        command = input("$ ")
        match command: 
            case "exit":
                sys.exit(0)
            
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
