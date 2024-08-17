import glob

import pandas as pd
import os
import warnings


def filemorph(from_file, sep, to, outdir=".", replace=False, try_encodings=['utf-8', 'latin1', 'iso-8859-1', 'cp1252'],
              **kwargs):
    to_path = os.path.join(os.path.dirname(from_file), outdir, os.path.basename(from_file).replace('.', '_') + f'.{to}')

    if not os.path.exists(os.path.dirname(to_path)):
        os.makedirs(os.path.dirname(to_path), exist_ok=True)

    if os.path.exists(to_path) and not replace:
        msg = f'Skipped creating `{to_path}`. File already exists. Use --replace argument to overwrite.'
        warnings.warn(msg, Warning)
        return

    print(f"- file: `{os.path.basename(from_file)}`")
    for encoding in try_encodings:
        try:
            df = pd.read_csv(from_file, sep=sep, encoding=encoding, **kwargs)
            break
        except Exception as e:
            print(f'    - Error processing with `{encoding}` encoding: {str(e)}')
            continue

    print(f"    - {df.shape} rows & columns.")
    if to == 'xlsx':
        df.to_excel(to_path, index=False)
    elif to == 'json':
        df.to_json(to_path, orient="records", indent=4)

    yield encoding, to_path


def dirmorph(args, **kwargs):
    path = os.path.join(args['dir'], args['file'])

    files = glob.glob(path)
    print(f"files: {len(files)}")

    for file in files:
        yield from filemorph(file, args['sep'], args['to'], outdir=args['outdir'], replace=args['replace'], **kwargs)

    return