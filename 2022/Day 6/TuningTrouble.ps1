$markerposition = 0
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 6\TuningTrouble.txt" | ForEach-Object{
    for($idx = 0; $idx -lt ($_.Length - 4); $idx++)
    {
        $substring = $_.Substring($idx, 4)
        if(($substring[0] -ne $substring[1]) -and ($substring[0] -ne $substring[2]) -and ($substring[0] -ne $substring[3]) -and ($substring[1] -ne $substring[2]) -and ($substring[1] -ne $substring[3]) -and ($substring[2] -ne $substring[3]))
        {
            $markerposition = $idx + 4
            break
        }
    }
}
Write-Host $markerposition
