import argparse
import sys


def wc(file, count_lines=True, count_words=True, count_characters=True):
    try:
        result = []
        lines = words = characters = 0
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)
        result.append(lines)
        result.append(words)
        result.append(characters)
        return result
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


def main():
    try:
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
                print(f"\t{counts[0]} {file.name}")
            elif not args.lines and args.words and not args.characters:
                print(f"\t{counts[1]} {file.name}")
            elif not args.lines and not args.words and args.characters:
                print(f"\t{counts[2]} {file.name}")
            elif args.lines and args.words and not args.characters:
                print(f"\t{counts[0]}\t{counts[1]} {file.name}")
            elif not args.lines and args.words and args.characters:
                print(f"\t{counts[1]}\t{counts[2]} {file.name}")
            elif args.lines and not args.words and args.characters:
                print(f"\t{counts[0]}\t{counts[2]} {file.name}")
            else:
                print(f"\t{counts[0]}\t{counts[1]}\t{counts[2]} {file.name}")
            total_lines += counts[0]
            total_words += counts[1]
            total_characters += counts[2]
        if len(args.files) > 1:
            if args.lines and not args.words and not args.characters:
                print(f"\t{total_lines} total")
            elif not args.lines and args.words and not args.characters:
                print(f"\t{total_words} total")
            elif not args.lines and not args.words and args.characters:
                print(f"\t{total_characters} total")
            elif args.lines and args.words and not args.characters:
                print(f"\t{total_lines}\t{total_words}\ total")
            elif not args.lines and args.words and args.characters:
                print(f"\t{total_words}\t{total_characters} total")
            elif args.lines and not args.words and args.characters:
                print(f"\t{total_lines}\t{total_characters} total")
            else:
                print(f"\t{total_lines}\t{total_words}\t{total_characters} total")
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
