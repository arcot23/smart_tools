from smart_tools.fusioner import filefusioner
import tomli
import os
import argparse

fusion_set = [
    {'column': 'new_col',
     'type': 'csv',
     'source': 'tvg-id,tvg-name,group-title,channel,domain,cat,url'}
]

config_file = r"C:\wip\smart_tools\smart_tools\fusioner\config\fusioner_config.toml"
file = r"C:\Users\prabhuramv\Downloads\tv_channels.csv"

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Input file")
    parser.add_argument("--sep", default=",", help="Column separator (default: ,)")
    parser.add_argument('--outfile', type= str, default='.\\.f\\fusioner_result',
                        help='Output directory and file name (default: .\\.f\\fusioner_result)')
    parser.add_argument('--config', default='.\config\\fusioner_config.toml',
                        help='Config file for ETL (default: `.\config\\fusioner_config.toml`)')

    args = vars(parser.parse_args())

    if not os.path.isabs(args['config']): args['config'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                        args['config'])

    if not os.path.exists(args['config']):
        print(f"Config file `{args['config']}` missing.")
        return 1

    print('**Arguments:**')
    for arg in args:
        print(f'- {arg}: `{args[arg]}`')

    with open(args['config'], 'rb') as f:
        configs = tomli.load(f)

    print('**Config:**')
    for config in configs:
        print(f'- {config}: `{configs[config]}`')

    print('**Process:**')
    df = filefusioner.filefusion(file, configs['nameset'], args['sep'])

    print('**Result:**')
    output_path = os.path.join(os.path.dirname(args["file"]), f'{args["outfile"]}.csv')

    if not os.path.exists(os.path.dirname(output_path)):
        print(f"- created directory `{os.path.dirname(output_path)}`.")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f'- {df.shape} rows & columns in `{output_path}`.')
    df.to_csv(output_path, index = False)
    return


if __name__ == '__main__':
    main()
