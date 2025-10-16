$Folder = ".\downloads"
$pythonExe = "C:\Users\prabhuramv\smart_tools\Scripts\python.exe"


Get-ChildItem -Path $Folder -Filter *.* | ForEach-Object {
    $File = $_.FullName
    Write-Host "Processing : " $File
    & $pythonExe ..\smart_tools\theydu\file_analyzer.py -f $File -o "./file_details"
}
