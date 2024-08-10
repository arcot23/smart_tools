# Dissector

## Using the dissector command-line tool

**dissector.exe** is a command-line tool to analyze CSV files. The input `file` can be a single file or files from a directory `dir` that have a common column separator `sep`. The _dissected_ results can be generated in the form of an excel file (`xlsx`) or text (`json` or `csv`). By default, the analysis is run on the entire content of the file i.e., without any filters. But `slicers` help slice data and run analysis. The output gives the following
information for each column element in the input file(s).

- column: column name.
- strlen: minimum and maximum string length.
- nnull: count of NANs and empty strings.
- nrow: number of rows.
- nunique: number of unique values.
- nvalue: number of rows with values.
- freq: frequency distribution of top n values. n is configured in `dissector_config.yaml`.
- sample: a sample of top n values. n is configured in `dissector_config.yaml`.
- symbols: non-alphanumic characters that are not in [a-zA-Z0-9]
- n: column order.
- filename: name of the input file from where the column was picked.
- filetype: file type to which the file is associated to (e.g., csv).

The output also presents other additional info:

- slice: The _slice_ used to select. Slices represents _filter conditions_ to select subsets of rows within a dataset.
- timestamp: file modified date timestamp of the input file.
- hash: md5 hash of the input file.
- size: file size of the input file in bytes.

```commandline
usage: dissector.py [-h] [-t {xlsx,json,csv}] [-s SEP]
                    [--slicers [SLICERS ...]] [-c [COLS ...]]
                    [--config CONFIG]
                    dir file

positional arguments:
  dir                   Input directory
  file                  Input file (for multiple files use wildcard)

optional arguments:
  -h, --help            show this help message and exit
  -t {xlsx,json,csv}, --to {xlsx,json,csv}
                        Save result to xlsx or json or csv (default: `xlsx`)
  -s SEP, --sep SEP     Column separator (default: `,`)
  --slicers [SLICERS ...]
                        Informs how to slice data (default: for no slicing)
  -c [COLS ...], --cols [COLS ...]
                        If not present, first row will be used for column
                        names. No duplicates allowed
  --config CONFIG       Config file for meta data (default:
                        `.\config\dissector_config.yaml`)
```

Before running the command, make sure a `yaml` config file is created and saved as `.\config\dissector_config.yaml` at
the working directory.

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

### Examples

Fetch `*.csv` from `.\temp` and dissect them with `,` as column separator.

```commandline
dissector .\temp *.csv -s ,
```

Fetch `myfile.text` from `c:\temp` and dissect the file with `;` as column separator.

```commandline
dissector c:\temp myfile.text -s ;
```

Fetch `myfile.text` from `c:\temp` and dissect the file with `;` as column separator by slicing the data with a filter on `COLUMN1 == 'VALUE'` and also without filtering any.

```commandline
dissector c:\temp myfile.text -s ; --slicers "" "COLUMN1 == 'VALUE'"
```

Fetch `myfile.text` from `c:\temp` and dissect the file with TAB `\t` as column separator by slicing the data with a filter on a column name that has a space in it    ` COLUMN 1 == 'VALUE'`.

```commandline
dissector c:\temp myfile.txt -sep ';' --slicers "" "`COLUMN 1` == 'VALUE'"
```

Using powershell, read the arguments from a text file.

```powershell
Get-Content args.txt | ForEach-Object {
    $arguments = $_ -split '#'
    & dissector.exe $arguments
}
```
Here is a sample args.txt file.

```
.\temp#*.csv#-s#,
```

# Morpher

## Using the morpher command-line tool

**morpher.exe** is a command-line tool to convert format of a file or files  in a directory that have a common column separator. For example, convert `file` delimited by `sep` in `dir` from  csv to `xlsx` or csv to `json`.

```text
usage: morpher.exe [-h] [--sep SEP] [--replace] [--to {xlsx,json}] dir file

positional arguments:
  dir               Input directory
  file              Input file or files (wildcard)

optional arguments:
  -h, --help        show this help message and exit
  --sep SEP         Column separator (default: ,)
  --replace         Replace output file if it already exists (default: false)
  --to {xlsx,json}  Morph to xlsx or json (default: xlsx)
```

# Comparator

## Using the morpher command-line tool

**comparator.exe** is a command-line tool to compare one file with another file.

```text
usage: comparator.exe [-h] [-s SEP] [-t {xlsx,json,csv}] file1 file2

positional arguments:
  file1                 File to compare
  file2                 File to compare with

optional arguments:
  -h, --help            show this help message and exit
  -s SEP, --sep SEP     Column separator (default: `,`)
  -t {xlsx,json,csv}, --to {xlsx,json,csv}
                        Save result to xlsx or json or csv (default: `xlsx`)
```