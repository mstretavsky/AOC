$markerposition = 0
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 6\TuningTrouble.txt" | ForEach-Object{
    for($idx = 0; $idx -lt ($_.Length - 14); $idx++)
    {
        $substring = $_.Substring($idx, 14)
        for($pos = 0; $pos -lt 13; $pos++)
        {
            $char = $substring[$pos]
            for($pos1 = $pos+1; $pos1 -lt 14; $pos1++)
            {
                if($char -eq $substring[$pos1])
                {
                    break
                }
            }
            if($pos1 -ne 14)
            {
                break
            }
        }
        if($pos -eq 13)
        {
            $markerposition = $idx + 14
            break
        }
    }
}
Write-Host $markerposition
