# prog/wc.py
import argparse
import sys


def wc(file):
    lines = words = characters = 0
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)
    return f"{lines}\t{words}\t{characters}"


def main():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input file",
    )
    args = parser.parse_args()
    result = wc(args.file)
    print(result)


if __name__ == "__main__":
    main()
