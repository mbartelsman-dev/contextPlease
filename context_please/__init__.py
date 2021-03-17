import argparse
from typing import Optional

from context_please.json_parser import *


def parse_arguments() -> argparse.Namespace:
    """
    Sets up argument parsing for the main program
    :return: A namespace object containing the read arguments and flags
    """
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
        default=None,
        dest='output',
        action='store',
        type=Optional[str],
        nargs=1,
        help='Base path for output files, defaults to same path as INPUT'
    )

    args = parser.parse_args()

    if args.output[0] is None:
        args.output[0] = args.input[0]

    return args


def main():
    args = parse_arguments()

    path = Path(args.input[0])
    print(path)
    data = read_file(path)
    obj = parse_data(data)
    print(args.input)
    print(args.output)


if __name__ == '__main__':
    """
    This tool allows the user to convert a simple JSON definition file into a context menu entry
    Entry
    """
    main()
