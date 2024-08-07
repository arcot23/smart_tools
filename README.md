
### Dissector

#### Using the dissector command-line tool

**Dissector** is a command-line tool that runs analysis on each column in a delimited file. The input can be a single file or a directory with multiple files. The output contains a table of the following each column in the input file:

- strlen: minimum and maximum string length of the column. 
- nnull: count of NAs and empty strings. 
- nrow: number of rows.
- nunique: number of unique values.
- nvalue: number of rows with values.
- freq: frequency distribution of top n values. n is configured in `dissector_config.yaml`.
- sample: a sample of top n values. n is configured in `dissector_config.yaml`.
- symbols: non-alphanumic characters that are not in [a-zA-Z0-9]

Additionally, the following columns:

- column: column name.
- n: column order.
- filename: name of the input file.
- filetype: file type to which the file is associated to (e.g., csv).
- slice: slice to which the row represents
- timestamp: file modified date.
- hash: md5 hash from the input file.
- size: filesize in bytes.

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
Before running the command, make sure a `yaml` config file is created and saved as `.\config\dissector_config.yaml` at the working directory.

```yaml
---
nsample: 10
read_csv:
  skipheader: 0
  skipfooter: 0
  engine: python
  encoding: 'utf-8'
  quotechar: '"'
  on_bad_lines: 'warn'
  dtype: 'str'
  keep_default_na: false

```

Here are some samples:

Fetch `*.csv` from `.\temp` and dissect them with delimiter `,`. 
```commandline
dissector .\temp *.csv -s ,
```
Fetch `myfile.text` from `c:\temp` and dissect the file with delimiter `;`.
```commandline
dissector c:\temp myfile.text -s ;
```
Fetch `myfile.text` from `c:\temp` and dissect the file with delimiter `;` by slicing the data without a filter and with a filter on `COLUMN1 == 'VALUE'`.
```commandline
dissector c:\temp myfile.text -s ; --slicers "" "COLUMN1 == 'VALUE'"
```
Fetch `myfile.text` from `c:\temp` and dissect the file with delimiter `;` by slicing the data without a filter and with a filter on a column name that has a space in it `COLUMN 1 == 'VALUE'`.
```commandline
dissector c:\temp myfile.text -sep ';' --slicers "" "`COLUMN 1` == 'VALUE'"
```

#### Using the dissector python libary

TODO

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

