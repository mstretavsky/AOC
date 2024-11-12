[System.Collections.ArrayList]$1Stack = @('D','B','J','V')
[System.Collections.ArrayList]$2Stack = @('P','V','B','W','R','D','F')
[System.Collections.ArrayList]$3Stack = @('R','G','F','L','D','C','W','Q')
[System.Collections.ArrayList]$4Stack = @('W','J','P','M','L','N','D','B')
[System.Collections.ArrayList]$5Stack = @('H','N','B','P','C','S','Q')
[System.Collections.ArrayList]$6Stack = @('R','D','B','S','N','G')
[System.Collections.ArrayList]$7Stack = @('Z','B','P','M','Q','F','S','H')
[System.Collections.ArrayList]$8Stack = @('W','L','F')
[System.Collections.ArrayList]$9Stack = @('S','V','F','M','R')
[System.Collections.ArrayList]$allstacks = $1Stack, $2Stack, $3Stack, $4Stack, $5Stack, $6Stack, $7Stack, $8Stack, $9Stack

Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 5\SupplyStacks.txt" | ForEach-Object{
    [string]$charstoremove = 'movefrmt'
    $procedure = $_.Split($charstoremove, [StringSplitOptions]::RemoveEmptyEntries)

    $upperidx = $allstacks.Item($procedure[1] - 1).Count - 1
    $loweridx = $allstacks.Item($procedure[1] - 1).Count - 1 - $procedure[0]
    for($idx = $upperidx; $idx -gt $loweridx; $idx--)
    {
        $allstacks.Item($procedure[2]-1).Add($allstacks[$procedure[1]-1][$idx])
        $allstacks.Item($procedure[1]-1).RemoveAt($idx)
    }
}
Write-Host $1Stack.Item($1Stack.Count-1)$2Stack.Item($2Stack.Count-1)$3Stack.Item($3Stack.Count-1)$4Stack.Item($4Stack.Count-1)$5Stack.Item($5Stack.Count-1)$6Stack.Item($6Stack.Count-1)$7Stack.Item($7Stack.Count-1)$8Stack.Item($8Stack.Count-1)$9Stack.Item($9Stack.Count-1)
