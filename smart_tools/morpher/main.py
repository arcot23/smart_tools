import argparse
from smart_tools.morpher.dirmorpher import dirmorph

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding positional arguments
    parser.add_argument("dir", help="Input directory")
    parser.add_argument("file", help="Input file or files (wildcard)")

    # Adding optional arguments
    parser.add_argument("--sep", default=",", help="Column separator")
    parser.add_argument("--replace", action="store_true", default=False, help="Replace output file if it already exists")
    parser.add_argument('--to', choices=['xlsx', 'json'], default='xlsx',
                        help='How to output dissected result: to_xls|to_json')

    args = vars(parser.parse_args())

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    print('**Process:**')
    for encoding, file in dirmorph(args):
        print(f"    - Created ({encoding})`{file}`")

    return

if __name__ == '__main__':
    main()
