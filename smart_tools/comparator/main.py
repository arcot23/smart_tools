import argparse
import json
from smart_tools.comparator import filecomparator

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file1', type=str, help='File to compare')
    parser.add_argument('file2', type=str, help='File to compare with')
    parser.add_argument('--sep', default=',', help='Column separator (default: `,`)')
    parser.add_argument('--to', choices=['xlsx', 'json', 'csv'], default='xlsx',
                        help='Save result to xlsx or json or csv (default: `xlsx`)')

    args = vars(parser.parse_args())

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    print('**Process:**')
    result = filecomparator.compare(args['file1'], args['file2'],sep=args['sep'])

    print('**Result:**')
    print(json.dumps(result, indent=4))

    return


if __name__ == '__main__':
    main()
