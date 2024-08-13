import argparse
import os
import yaml
from smart_tools.morpher.dirmorpher import dirmorph

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding positional arguments
    parser.add_argument("dir", help="Input directory")
    parser.add_argument("file", help="Input file or files (wildcard)")

    # Adding optional arguments
    parser.add_argument("--sep", default=",", help="Column separator (default: ,)")
    parser.add_argument("--replace", action="store_true", default=False, help="Replace output file if it already exists (default: false)")
    parser.add_argument('--to', choices=['xlsx', 'json'], default='xlsx',
                        help='Morph to xlsx or json (default: xlsx)')
    parser.add_argument('--outdir', type= str, default='.',
                        help='Output directory (default: . [current directory])')
    parser.add_argument('--config', default='.\config\morpher_config.yaml',
                        help='Config file for meta data (default: `.\config\morpher_config.yaml`)')

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
    for encoding, file in dirmorph(args, **configs['read_csv']):
        print(f"    - Created ({encoding})`{file}`")

    return

if __name__ == '__main__':
    main()
