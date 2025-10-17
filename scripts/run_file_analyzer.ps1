Set-Location -Path "C:\wip\smart_tools"

$Folder = ".\smart_tools\theydu\downloads"
$pythonExe = "C:\Users\prabhuramv\smart_tools\Scripts\python.exe"

$env:PYTHONPATH = "C:\wip\smart_tools;$env:PYTHONPATH"

Get-ChildItem -Path $Folder -Filter *.* | ForEach-Object {
    $File = $_.FullName
    Write-Host "Processing : " $File
    & $pythonExe .\smart_tools\theydu\file_analyzer.py -f $File -o ".\smart_tools\theydu\file_details"
}
