import os
import argparse
import yaml

from smart_tools.dissector.dirdissector import dissect_from_dir


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', type=str, help='Input directory')
    parser.add_argument('file', type=str, help='Input file (for multiple files use wildcard)')
    # parser.add_argument('--from', choices=['csv', 'xls'], default='csv',
    #                     help='How to process files: as_csv|as_xls')
    parser.add_argument('-t' '--to', choices=['xlsx', 'json', 'csv'], default='xlsx',
                        help='Dissected as one of: xlsx or json. Default is xlsx.')
    parser.add_argument('-s','--sep', default=',', help='Column separator')
    parser.add_argument('--slicers', nargs='*', default=[''],
                        help='Informs how to slice data. Default is "" for no slicing.')
    parser.add_argument('-c', '--cols', nargs='*',
                        help='If present, first row will not be used for column names. No duplicates allowed.')
    parser.add_argument('--config', default='.\config\dissector_config.yaml', help='Config file for meta data. Defaults to `.\config\dissector_config.yaml`')

    args = vars(parser.parse_args())

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    with open(args['config'], 'r') as f:
        configs = yaml.safe_load(f)

    print('**Config:**')
    for config in configs:
        print(f'- {config}: `{configs[config]}`')

    print('**Process:**')
    df_all = dissect_from_dir(args, configs)

    print('**Result:**')
    output_path = os.path.join(args['dir'], f'dissect_result.{args["to"]}')
    print(f'- {df_all.shape} rows & columns in `{output_path}`.')
    if args['to'] == 'xlsx':
        df_all.to_excel(output_path, index=False)
    elif args['to'] == 'json':
        df_all.to_json(output_path, orient='records', indent=4)
    elif args['to'] == 'csv':
        df_all.to_csv(output_path, index=False)


if __name__ == '__main__':
    main()
