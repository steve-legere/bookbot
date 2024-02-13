import argparse
from sys import version_info

if version_info < (3, 9):
    exit("Python 3.9 or higher is required to run this script.")

def init_parser():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Provides word and character reports on a text document.')

    # Add arguments
    parser.add_argument('file', type=str, help='File path of book to parse')

    # Parse the arguments
    args = parser.parse_args()

    return parser, args

def main():
    parser, args = init_parser()
    print(f"Got {args.book}")

if __name__ == '__main__':
    main()