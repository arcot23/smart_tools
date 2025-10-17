Set-Location -Path "C:\wip\smart_tools"

# Define the path to your CSV file containing URLs
$csvFilePath = ".\config\download_list.csv"

$pythonExe = "C:\Users\prabhuramv\smart_tools\Scripts\python.exe"

Write-Host "Download processing started."

# Import the CSV file
$csvData = Import-Csv -Path $csvFilePath

# Loop through each row in the CSV data
foreach ($row in $csvData) {
    # Access individual column values using dot notation (e.g., $row.ColumnName)
    # Replace 'Column1', 'Column2', etc., with the actual header names from your CSV
    $argument1 = $row.url
    # Add more arguments as needed based on your CSV structure

    # Construct the arguments array for the program
    # This example passes two arguments. Adjust as needed.
    $programArguments = @($argument1, "-o", ".\smart_tools\theydu\downloads")

    # Execute the program with the constructed arguments
    # Use Start-Process for launching external executables
    & $pythonExe .\smart_tools\theydu\downloader.py $programArguments



    # -NoNewWindow prevents a new console window from appearing for the program
    # -Wait makes the script pause until the external program finishes execution
}

Write-Host "Download processing complete."