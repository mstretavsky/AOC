$headhorpos = 0
$headverpos = 0
$tailhorpos = 0
$tailverpos = 0
$coveredpos = @{'0:0' = 0}
$filecontent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 9\RopeBridge.txt"
for($lineIdx = 0; $lineIdx -lt $filecontent.Length; $lineIdx++)
{
    $splits = $filecontent[$lineIdx].Split(' ')
    for($i = 0; $i -lt $splits[1]; $i++)
    {
        if($splits[0] -eq 'R')
        {
            $headhorpos++
        }
        elseif ($splits[0] -eq 'L') 
        {
            $headhorpos--
        }
        elseif ($splits[0] -eq 'U') 
        {
            $headverpos++
        }
        else     
        {#down
            $headverpos--
        }
        if(($tailverpos - $headverpos) -gt 1)
        {
            $tailhorpos = $headhorpos
            $tailverpos = $headverpos+1
        }
        elseif (($headverpos - $tailverpos) -gt 1) 
        {
            $tailhorpos = $headhorpos
            $tailverpos = $headverpos-1
        }
        elseif(($tailhorpos - $headhorpos) -gt 1)
        {
            $tailverpos = $headverpos
            $tailhorpos = $headhorpos+1
        }
        elseif(($headhorpos - $tailhorpos) -gt 1)
        {
            $tailverpos = $headverpos
            $tailhorpos = $headhorpos-1
        }

        $formpos = ''+$tailhorpos+':'+$tailverpos+''
        if(!$coveredpos.ContainsKey($formpos))
        {
            $coveredpos.Add($formpos, 0)
        }
    }
}
Write-Host $coveredpos.Keys.Count