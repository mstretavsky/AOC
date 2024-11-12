function Get-RegisterValue($content, $targetcycle)
{
    $registervalue = 1
    $cycles = 0
    for($lineIdx = 0; $lineIdx -lt $filecontent.Length; $lineIdx++)
    {
        $linecontent = $filecontent[$lineIdx]
        $pair = $linecontent.Split(' ')
        if($pair[0] -eq 'addx')
        {
            $cycles += 2
        }
        else
        {#noop
            $cycles += 1
        }

        if($cycles -ge $targetcycle)
        {
            break
        }
        $registervalue += $pair[1]
    }
    return $registervalue
}



$signalstrength = 0
$filecontent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 10\CathodeRayTube.txt"
$targetcycles = @(20, 60, 100, 140, 180, 220)
foreach($targetcycle in $targetcycles)
{
    $registervalue = Get-RegisterValue -content $filecontent -targetcycle $targetcycle
    $signalstrength += ($targetcycle * $registervalue)
}

Write-Host $signalstrength