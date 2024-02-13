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

def process_text(text):
    words = text.split()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return words, chars

def main():
    parser, args = init_parser()
    try:
        with open(args.file) as f:
            text = f.read()
            words, chars = process_text(text)
            print(f"There are {len(words)} words and {len(chars)} characters.")      
    except FileNotFoundError as e:
        exit(e)

if __name__ == '__main__':
    main()