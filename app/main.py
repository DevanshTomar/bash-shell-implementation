from ast import arguments
import sys


built_in = set([
    "type",
    "echo",
    "exit"
])

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
            case "type":    
                commands_to_check = args.split(" ")
                for command in commands_to_check:
                    if not command: continue
            
                    if command not in built_in:
                        print(f"{command}: not found")
                        continue

                    print(f"{command} is a shell builtin")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
