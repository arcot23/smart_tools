import sys
import os
from datetime import datetime
import builtins

def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False, log_file=os.path.join(os.path.dirname(os.getcwd()),".log", "smart_tools.log")):
    builtins.print(log_file)
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Prepare the output string
    output = sep.join(map(str, objects)) + end

    # Print to console
    builtins.print(output, end='', file=file, flush=flush)

    # Log to file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as log:
        log.write(f"[{timestamp}] {output}")

    # Flush the file if required
    if flush:
        log.flush()