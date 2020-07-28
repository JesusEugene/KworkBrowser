import sys


from src.core import execute_from_command_line


def main():
    execute_from_command_line(sys.argv[1:])

if __name__ == "__main__":
    main()