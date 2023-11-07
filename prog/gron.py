# prog/gron.py
import argparse
import json
import sys


def gron(file):
    data = json.load(file)
    formatted_json = format_json(data, outer=True)
    return formatted_json


def format_json(json_obj, parent_key="", sep=".", outer=False):
    formatted = ""
    if outer:
        formatted += "json = {};\n"
        parent_key = "json"
    for key in sorted(json_obj.keys()):  # Sort keys alphabetically
        value = json_obj[key]
        current_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            formatted += f"{current_key} = {{}};\n"
            formatted += format_json(value, current_key, sep=sep)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                item_key = f"{current_key}[{i}]"
                formatted += format_json({item_key: item}, sep="") + "\n"
        else:
            formatted += f"{current_key} = {json.dumps(value)};\n"
    return formatted.strip()


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
