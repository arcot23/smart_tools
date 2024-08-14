import argparse
import os
from smart_tools.aggregator import fileaggregator

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', type=str, help='Input directory')
    parser.add_argument('file', type=str, help='Input file or files (for multiple files use wildcard)')
    parser.add_argument('--sep', default=',', help='Column separator (default: `,`)')
    parser.add_argument('--to', choices=['xlsx', 'json', 'csv'], default='xlsx',
                        help='Save result to xlsx or json or csv (default: `xlsx`)')
    parser.add_argument('--outfile', type= str, default='.\.a\\aggregated_result',
                        help='Output directory and file name (default: .\dissect_result)')

    args = vars(parser.parse_args())

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    print('**Process:**')
    df_all = fileaggregator.aggregate_files(dir=args['dir'], file_wildcard=args['file'], sep=args['sep'],include_filename=True)

    print('**Result:**')
    output_path = os.path.join(args['dir'], f'{args["outfile"]}.{args["to"]}')

    if not os.path.exists(os.path.dirname(output_path)):
        print(f"- created directory `{os.path.dirname(output_path)}`.")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f'- {df_all.shape} rows & columns in `{output_path}`.')
    if args['to'] == 'xlsx':
        df_all.to_excel(output_path, index=False)
    elif args['to'] == 'json':
        df_all.to_json(output_path, orient='records', indent=4)
    elif args['to'] == 'csv':
        df_all.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()
