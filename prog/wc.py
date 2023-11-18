import argparse
import sys


def wc(file, count_lines=True, count_words=True, count_characters=True):
    lines = words = characters = 0
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)
    result = []
    if count_lines:
        result.append(lines)
    else:
        result.append(0)
    if count_words:
        result.append(words)
    else:
        result.append(0)
    if count_characters:
        result.append(characters)
    else:
        result.append(0)
    return result


def main():
    parser = argparse.ArgumentParser(description="Word count utility")
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="Count only lines",
    )
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="Count only words",
    )
    parser.add_argument(
        "-c",
        "--characters",
        action="store_true",
        help="Count only characters",
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=argparse.FileType("r"),
        default=[sys.stdin],
        help="Input files",
    )
    args = parser.parse_args()
    total_lines = total_words = total_characters = 0
    if not any([args.lines, args.words, args.characters]):
        args.lines = args.words = args.characters = True
    for file in args.files:
        counts = wc(file, args.lines, args.words, args.characters)
        if args.lines and not args.words and not args.characters:
            if len(args.files) == 1:
                print(f"{counts[0]}")
            else:
                print(f"{counts[0]}\t{file.name}")
        elif args.words and not args.lines and not args.characters:
            if len(args.files) == 1:
                print(f"{counts[1]}")
            else:
                print(f"{counts[1]}\t{file.name}")
        elif args.characters and not args.lines and not args.words:
            if len(args.files) == 1:
                print(f"{counts[2]}")
            else:
                print(f"{counts[2]}\t{file.name}")
        else:
            print(f"{counts[0]}\t{counts[1]}\t{counts[2]}\t{file.name}")
        total_lines += counts[0]
        total_words += counts[1]
        total_characters += counts[2]
    if len(args.files) > 1:
        if args.lines and not args.words and not args.characters:
            print(f"{total_lines}\ttotal")
        elif args.words and not args.lines and not args.characters:
            print(f"{total_words}\ttotal")
        elif args.characters and not args.lines and not args.words:
            print(f"{total_characters}\ttotal")
        else:
            print(f"{total_lines}\t{total_words}\t{total_characters}\ttotal")


if __name__ == "__main__":
    main()
