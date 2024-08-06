
### dissector

```commandline
usage: dissector [-h] [-t--to {xlsx,json,csv}] [-s SEP]
                    [--slicers [SLICERS ...]] [-c [COLS ...]]
                    [--config CONFIG]
                    dir file

positional arguments:
  dir                   Input directory
  file                  Input file (for multiple files use wildcard)

optional arguments:
  -h, --help            show this help message and exit
  -t--to {xlsx,json,csv}
                        Dissected as one of: xlsx or json. Default is xlsx.
  -s SEP, --sep SEP     Column separator
  --slicers [SLICERS ...]
                        Informs how to slice data. Default is "" for no
                        slicing.
  -c [COLS ...], --cols [COLS ...]
                        If present, first row will not be used for column
                        names. No duplicates allowed.
  --config CONFIG       Config file for meta data. Defaults to
                        `.\config\dissector_config.yaml`
```

Examples:

```commandline
> dissector .\temp *.csv -s ,

> dissector c:\temp myfile.text -s ;

> dissector c:\temp myfile.text -s ; --slicers "" "COLUMN1 == 'VALUE'"

> dissector c:\temp myfile.text -s ; --slicers "" "`COLUMN 1` == 'VALUE'"

```

### morpher


```text
usage: morpher [-h] [--sep SEP] [--replace] [--to {xlsx,json}] dir file

positional arguments:
  dir               Input directory
  file              Input file or files (wildcard)

optional arguments:
  -h, --help        show this help message and exit
  --sep SEP         Column separator
  --replace         Replace output file if it already exists
  --to {xlsx,json}  How to output dissected result: to_xls|to_json
```

### banking

