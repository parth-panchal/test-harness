# prog/ungron.py
import argparse
import json
import sys


def ungron(file):
    flat_json = {}
    for line in file:
        key, _, value = line.strip().partition("=")
        set_nested_key(flat_json, key.strip().split("."), value.strip())

    return json.dumps(flat_json, indent=2)


def set_nested_key(dictionary, keys, value):
    for key in keys[:-1]:
        dictionary = dictionary.setdefault(key, {})
    dictionary[keys[-1]] = value


def main():
    parser = argparse.ArgumentParser(description="JSON unflattening utility")
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input file",
    )
    args = parser.parse_args()

    result = ungron(args.file)
    print(result)


if __name__ == "__main__":
    main()
