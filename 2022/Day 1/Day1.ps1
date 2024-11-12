[int]$bucketCalories = 0
$intarray = New-Object System.Collections.ArrayList
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 1\input values.txt" | ForEach-Object{
    if([string]::IsNullOrEmpty($_))
    {
        $intarray.Add($bucketCalories) | Out-Null
        $bucketCalories = 0
    }
    else
    {
        $bucketCalories += $_
    }
}
Write-Host "Maximum of calories is:"
$intarray | sort | select -Last 1

Write-Host "First 3 highest amounts of calories are:"
$intarray | sort | select -Last 3