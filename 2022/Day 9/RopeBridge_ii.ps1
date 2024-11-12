function MoveKnots($headknotpos, $tailknotpos) 
{
    $headknotpossplit = $headknotpos.Split(':')
    [int]$headropeknothorpos = $headknotpossplit[0]
    [int]$headropeknotverpos = $headknotpossplit[1]

    $tailknotpossplit = $tailknotpos.Split(':')
    [int]$tailropeknothorpos = $tailknotpossplit[0]
    [int]$tailropeknotverpos = $tailknotpossplit[1]

    $verdifference = $headropeknotverpos - $tailropeknotverpos
    $verchange = -1
    if($verdifference -gt 0)
    {
        $verchange = 1
    }
    $hordifference = $headropeknothorpos - $tailropeknothorpos
    $horchange = -1
    if($hordifference -gt 0)
    {
        $horchange = 1
    }
    if(([math]::Abs($verdifference) -gt 1) -and ([math]::Abs($hordifference) -gt 1))
    {

        $tailropeknothorpos += $horchange
        $tailropeknotverpos += $verchange
    }
    elseif([math]::Abs($verdifference) -gt 1)
    {
        $tailropeknothorpos = $headropeknothorpos
        $tailropeknotverpos += $verchange
    }
    elseif([math]::Abs($hordifference) -gt 1)
    {
        $tailropeknotverpos = $headropeknotverpos
        $tailropeknothorpos += $horchange
    }
    return ''+$tailropeknothorpos+':'+$tailropeknotverpos+''
}

$coveredpos = @{'0:0' = 0}
$ropeknots = @('0:0','0:0','0:0','0:0','0:0','0:0','0:0','0:0','0:0','0:0')
$filecontent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 9\RopeBridge.txt"
for($lineIdx = 0; $lineIdx -lt $filecontent.Length; $lineIdx++)
{
    $splits = $filecontent[$lineIdx].Split(' ')
    for($i = 0; $i -lt $splits[1]; $i++)
    {
        $headropeknotsplit = $ropeknots[0].Split(':')
        [int]$headropeknothorpos = $headropeknotsplit[0]
        [int]$headropeknotverpos = $headropeknotsplit[1]
        if($splits[0] -eq 'R')
        {
            $headropeknothorpos++
        }
        elseif ($splits[0] -eq 'L') 
        {
            $headropeknothorpos--
        }
        elseif ($splits[0] -eq 'U') 
        {
            $headropeknotverpos++
        }
        else     
        {
            $headropeknotverpos--
        }
        $ropeknots[0] = ''+$headropeknothorpos+':'+$headropeknotverpos+''
        for($j = 0; $j -lt 9; $j++)
        {
            $ropeknots[$j+1] = MoveKnots -headknotpos $ropeknots[$j] -tailknotpos $ropeknots[$j+1]
        }
        if(!$coveredpos.ContainsKey($ropeknots[$ropeknots.GetUpperBound(0)]))
        {
            $coveredpos.Add($ropeknots[$ropeknots.GetUpperBound(0)], 0)
        }
    }
}
Write-Host $coveredpos.Keys.Count