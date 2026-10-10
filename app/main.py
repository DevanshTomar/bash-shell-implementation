import os
import sys
from pathlib import Path

BUILTIN = ([
    "type",
    "echo",
    "exit"
])


def find_executable(name: str) -> str | None:
    for directory in os.environ.get("PATH", "").split(os.pathsep):
        path: Path = Path(directory) / name
        if path.is_file() and os.access(path, os.X_OK):
            return str(path)
    return None


def main():
    while True:
        try:
            command = input("$ ")
        except EOFError:
            break 
            
        name, _, args = command.partition(" ")
        if not name:
            continue
            
        match name:
            case "exit":
                sys.exit(0)
            case "echo":
                print(args)
            case "type":    
                for target in args.split():
                    if target in BUILTIN:
                        print(f"{target} is a shell builtin")
                    elif path := find_executable(target):
                        print(f"{target} is {path}")
                    else:
                        print(f"{target}: not found")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
