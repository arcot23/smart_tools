import glob
import os
import warnings
from smart_tools.morpher.csvmorpher import filemorph

def dirmorph(args):
    path = os.path.join(args['dir'], args['file'])

    files = glob.glob(path)
    print(f"files: {len(files)}")

    for file in files:
        yield from filemorph(file, args['sep'], args['to'], args['replace'], outdir=args['outdir'])

    return
