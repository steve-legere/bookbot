import argparse
from sys import version_info

if version_info < (3, 9):
    exit("Python 3.9 or higher is required to run this script.")

def init_parser():
    parser = argparse.ArgumentParser(description='Provides word and character reports on a text document.')
    parser.add_argument('file', type=str, help='File path of book to parse')
    args = parser.parse_args()
    return parser, args

def process_text(text):
    words = text.split()
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return words, sorted_chars

def print_report(name, words, chars):
    print(f"--- Begin report of {name} ---")
    print(f"{len(words)} words found in the document\n")
    for char, num in chars.items():
        print(f"The {repr(char)} character was found {num} times")
    print("--- End report ---")

def main():
    parser, args = init_parser()
    try:
        with open(args.file) as f:
            text = f.read()
            words, chars = process_text(text)
            print_report(args.file, words, chars)    
    except FileNotFoundError as e:
        exit(e)

if __name__ == '__main__':
    main()