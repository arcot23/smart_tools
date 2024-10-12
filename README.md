# smart_tools: tools to make data analysis easy

**smart_tools** contains a collection of command-line tools developed in Python. It aims in performing common data analyst activities easier.

# Table of Contents

- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [How to use command-line tools](#how-to-use-command-line-tools)
- [dissector](#dissector), analyze one or more files for data profiling
- [morpher](#morpher), convert files from one format to another
- [comparator](#comparator), compare two files for differences
- [aggregator](#comparator), append two or more files row-wise
- [fusioner](#fusioner), transform columns in a file

# Where to get it

The source code is currently hosted on GitHub at: https://github.com/arcot23/smart_tools

Binary installers for the released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/smart-tools/)

```text
# PyPI
python -m pip install smart-tools
```

# Dependencies

- [pandas](https://pandas.pydata.org/)
- [pyyaml](https://pyyaml.org/)

# How to use command-line tools

To get help, simply run respective executable with `-h` argument from your terminal. For example dissector can be run with `dissector.exe -h`.  Run the command with positional arguments which are mandatory, but review the optional arguments `dissector.exe dir file*.txt`.

To easily access these command-line tools, add the executable's directory to PATH (in Windows) environment variable `$Env:PATH`. Most tools also depends on a `config.yaml` file for certain additional settings. 

```text
dissector.exe
morpher.exe
comparator.exe
aggregator.exe
fusioner.exe
└── config/
    ├── dissector_config.yaml
    ├── morpher_config.yaml
    ├── comparator_config.yaml
    ├── aggregator_config.yaml
    ├── fusioner_config.yaml
    └── ...
```

All command-line tools takes an input and generates an output. Input is typically a directory `dir` together with a file or files `file`. Output is created under `dir` which comprises an output directory and output files. `dir `can be a relative path from where the command is run or an absolute path. The folder hierarchy listed below shows the structure.

```text
dir
├── file1.txt
├── file2.txt
├── ...
├── .d/
│   └── dissector_result.xlsx
├── .m/
│   └── morpher_result.xlsx
├── .c/
│   └── comparator_result.xlsx
├── .a/
│   └── aggregator_result.xlsx
└── .f/
    └── fusioner_result.xlsx
```

# Dissector

**dissector.exe** is a command-line tool to analyze CSV files. The input `file` can be a single file or files from a directory `dir` that have a common column separator `sep`. The _dissected_ results can be generated in the form of an excel file (`xlsx`) or text (`json` or `csv`). By default, the analysis is run on the entire content of the file i.e., without any filters. But `slicers` help slice data and run analysis. 


```commandline
usage: dissector.exe [-h] [--to {xlsx,json,csv}] [--sep SEP]
                    [--slicers [SLICERS ...]] [--nsample NSAMPLE]
                    [--outfile OUTFILE] [--config CONFIG]
                    dir file

positional arguments:
  dir                   Input directory
  file                  Input file (for multiple files use wildcard)

optional arguments:
  -h, --help            show this help message and exit
  --to {xlsx,json,csv}  Save result to xlsx or json or csv (default: xlsx)
  --sep SEP             Column separator (default: ,)
  --slicers [SLICERS ...]
                        Informs how to slice data (default: for no slicing)
  --nsample NSAMPLE     Number of samples (default: 10)
  --outfile OUTFILE     Output file name (default: dissect_result)
  --config CONFIG       Config file for meta data (default:
                        `.\config\dissector_config.yaml`)
```


The output gives the following information for each column element in the input file(s).

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

Ensure that a yaml config file is present at `.\config\dissector_config.yaml` in relation to `dissector.exe` prior to executing the command.

```yaml
---
read_csv:
  skiprows: 0
  skipfooter: 0
  engine: 'python' # {'c', 'python', 'pyarrow'}
  encoding: 'latin-1' # {'utf-8', 'latin-1'}
  quotechar: '"'
  on_bad_lines: 'warn' # {'error', 'warn', 'skip'}
  dtype: 'str'
  keep_default_na: false
```

**Examples**

- Fetch `*.csv` from `.\temp` and dissect them with `,` as column separator.

    `dissector .\temp *.csv -s ,`

- Fetch `myfile.text` from `c:\temp` and dissect the file with `;` as column separator.

    `dissector c:\temp myfile.text -s ;`

- Fetch `myfile.text` from `c:\temp` and dissect the file with `;` as column separator by slicing the data with a filter on `COLUMN1 == 'VALUE'` and also without filtering any.

    `dissector c:\temp myfile.text -s ; --slicers "" "COLUMN1 == 'VALUE'"`

- Fetch `myfile.text` from `c:\temp` and dissect the file with TAB `\t` as column separator by slicing the data with a filter on a column name that has a space in it    ` COLUMN 1 == 'VALUE'`.

     `dissector c:\temp myfile.txt -sep ';' --slicers "" "`COLUMN 1` == 'VALUE'"`

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

# Aggregator

**aggregator.exe** is a command-line tool to aggregate two or more file together into one.

```text
usage: aggregator.py [-h] [--sep SEP] [--to {xlsx,json,csv}]
                     [--outfile OUTFILE] [--config CONFIG]
                     dir file

positional arguments:
  dir                   Input directory
  file                  Input file or files (for multiple files use wildcard)

optional arguments:
  -h, --help            show this help message and exit
  --sep SEP             Column separator (default: `,`)
  --to {xlsx,json,csv}  Save result to xlsx or json or csv (default: `xlsx`)
  --outfile OUTFILE     Output directory and file name (default:
                        .\.a\aggregated_result)
  --config CONFIG       Config file for meta data (default:
                        `.\config\aggregator_config.yaml`)
```

# Fusioner

**aggregator.exe** is a command-line tool to aggregate two or more file together into one.

```text
usage: fusioner.py [-h] [--sep SEP] [--outfile OUTFILE] [--config CONFIG] file

positional arguments:
  file               Input file

optional arguments:
  -h, --help         show this help message and exit
  --sep SEP          Column separator (default: ,)
  --outfile OUTFILE  Output directory and file name (default:
                     .\.f\fusioner_result)
  --config CONFIG    Config file for ETL (default:
                     `.\config\fusioner_config.toml`)

```