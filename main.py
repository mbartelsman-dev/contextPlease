import json
import argparse
from typing import Any


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Convert a JSON-formatted file into a registry definition for a '
                                                 'context menu')
    parser.add_argument(
        'input',
        metavar='INPUT',
        action='store',
        type=str,
        nargs=1,
        help='Path to the JSON file'
    )
    parser.add_argument(
        '-o',
        metavar='OUTPUT',
        default='output.reg',
        dest='output',
        action='store',
        type=str,
        nargs=1,
        help='Path to where the .reg file should be saved to, defaults to output.reg'
    )
    return parser.parse_args()


def parse_json_input(file_path: str) -> Any:
    with open(file_path) as file:
        data = json.load(file)
    return data


def validate_input(obj):
    if obj['entries'] is not None:
        pass
    elif obj['cmd'] is not None:
        pass
    else:
        raise Exception("Root object must have either entries or a command")
    pass


if __name__ == '__main__':
    """
    This tool allows the user to convert a simple JSON definition file into a context menu entry
    Entry
    """
    args = parse_arguments()
    obj = parse_json_input(args.input[0])
    print(obj)
    validate_input(obj)
    print(args.input)
    print(args.output)