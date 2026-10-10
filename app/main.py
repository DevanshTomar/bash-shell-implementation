import sys


def main():
    while True:
        command = input("$ ")
        name, _, args = command.partition(" ")

        match name:
            case "exit":
                sys.exit(0)
            case "echo":
                if not args:
                    continue
                print(args)
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
