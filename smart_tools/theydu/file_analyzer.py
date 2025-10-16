import argparse
import sys
import hashlib
import json
from pathlib import Path
from datetime import datetime
import mimetypes

# --- Constants ---
# A reasonable block size for reading large files to calculate hash
BLOCK_SIZE = 65536


# --- Core Functionality ---

def calculate_file_checksum_and_size(file_path: Path) -> tuple[str, int]:
    """Calculates the SHA256 hash and size in bytes for a local file."""
    sha256_hash = hashlib.sha256()
    file_size = 0

    try:
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks
            while True:
                data = f.read(BLOCK_SIZE)
                if not data:
                    break
                sha256_hash.update(data)
                file_size += len(data)

        return sha256_hash.hexdigest(), file_size

    except FileNotFoundError:
        # Re-raise with a more specific error or handle it as needed
        raise FileNotFoundError(f"Error: Local file not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred during file processing: {e}", file=sys.stderr)
        raise


def analyze_file(file: str, output_dir: str) -> Path:
    """
    Analyzes a local file, generates metadata, and writes it to a JSON file.

    Args:
        file: The local file path (must be local for checksum/size calculation).

    Returns:
        The path to the generated metadata file.
    """

    # 1. Prepare Paths
    input_file_path = Path(file)

    # Ensure the file exists before proceeding with analysis
    if not input_file_path.is_file():
        raise FileNotFoundError(f"Error: File does not exist or is not a file: {file}")

    # Use pathlib to get the file stem for the output file name
    output_file_name = f"{input_file_path.stem}_details.txt"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_file_path = Path(output_dir) / output_file_name
    mime_type, encoding = mimetypes.guess_type(file)

    # 2. Gather Data
    checksum, size_bytes = calculate_file_checksum_and_size(input_file_path)

    # Get current time in ISO format for consistency
    download_datetime = datetime.now().isoformat()

    # 3. Create Metadata Dictionary
    metadata = {
        "file_name": input_file_path.name,
        "mime_type": mime_type,
        "encoding": encoding,
        "full_file_path": str(input_file_path.resolve()),  # Resolve to get the absolute path
        "SHA256": checksum,
        "file_size_in_bytes": size_bytes,
        "file_download_datetime": download_datetime
    }

    # 4. Write to JSON file
    try:
        with open(output_file_path, 'w') as outfile:
            # Use json.dumps for a nicely formatted, readable output file
            json.dump(metadata, outfile, indent=4)

        print(f"\n✅ Successfully created metadata file at: {output_file_path.resolve()}")
        return output_file_path

    except Exception as e:
        print(f"Error writing metadata file: {e}", file=sys.stderr)
        raise


# --- Argparse Snippet (Unchanged) ---
def main():
    """Parses command line arguments and initiates file analysis."""
    parser = argparse.ArgumentParser(
        description="Analyze a local sanctions list file and generate a metadata JSON file.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-f', '--file',
        type=str,
        required=True,
        help="The local file path for the sanctions list data (e.g., ./sdn.csv).",
        metavar='LOCAL_FILE_PATH'
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default=".",
        help="Target directory to save the analysis file (default: .)."
    )

    args = parser.parse_args()

    # The original function call
    return analyze_file(file=args.file, output_dir=args.output_dir)


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Program failed: {e}", file=sys.stderr)
        sys.exit(1)