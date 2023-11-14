# prog/gron.py
import argparse
import json
import sys


def walk(obj, name):
    if obj is None:
        return f"{name} = null;"
    elif isinstance(obj, bool):
        return f"{name} = {str(obj).lower()};"
    elif isinstance(obj, str):
        return f'{name} = "{obj}";'
    elif isinstance(obj, bytes):
        return f'{name} = "{obj!r}";'
    elif isinstance(obj, dict):
        res = []
        res.append(f"{name} = {{}};")
        for k, v in sorted(obj.items()):
            res.append(walk(v, name + convert("." + k)))
        return "\n".join(sorted(res))
    elif isinstance(obj, (list, tuple)):
        res = []
        res.append(f"{name} = [];")
        for i, e in enumerate(obj):
            res.append(walk(e, name + convert(str([i]))))
        return "\n".join(res)
    else:
        return f"{name} = {obj!r};"


def convert(name):
    if "-" in name or " " in name:
        return '["{}"]'.format(name[1:])
    return name


def gron(file):
    data = json.load(file)
    output = walk(data, "json")
    return output


def main():
    parser = argparse.ArgumentParser(description="JSON flattening utility")
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input file",
    )
    args = parser.parse_args()
    result = gron(args.file)
    print(result)


if __name__ == "__main__":
    main()
