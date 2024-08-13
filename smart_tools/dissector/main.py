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
    parser.add_argument('--to', choices=['xlsx', 'json', 'csv'], default='xlsx',
                        help='Save result to xlsx or json or csv (default: xlsx)')
    parser.add_argument('--sep', default=',', help='Column separator (default: ,)')
    parser.add_argument('--slicers', nargs='*', default=[''],
                        help='Informs how to slice data (default: '' for no slicing)')
    parser.add_argument('--nsample', type= int, default='10',
                        help='Number of samples (default: 10)')
    parser.add_argument('--outfile', type= str, default='dissect_result',
                        help='Output file name (default: dissect_result)')
    parser.add_argument('--config', default='.\config\dissector_config.yaml',
                        help='Config file for meta data (default: `.\config\dissector_config.yaml`)')

    args = vars(parser.parse_args())

    if not os.path.isabs(args['config']): args['config'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                        args['config'])

    if not os.path.exists(args['config']):
        print(f"Config file `{args['config']}` missing.")
        return 1

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    with open(args['config'], 'r') as f:
        configs = yaml.safe_load(f)

    print('**Config:**')
    for config in configs:
        print(f'- {config}: `{configs[config]}`')

    print('**Process:**')
    df_all = dissect_from_dir(dir=args['dir'], file=args['file'], sep=args['sep'], nsample=args['nsample'],
                              slicers=args['slicers'], **configs['read_csv'])

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

    return 0


if __name__ == '__main__':
    main()
