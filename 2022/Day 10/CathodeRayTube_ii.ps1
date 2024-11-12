
$cycles = 0
$spritestaticwindow = '...........................................###.....................................................'
$spritewindowstartpos = 43
$spritecurrentwindow = $spritestaticwindow.Substring($spritewindowstartpos, 40)
$crtrows = ''
$filecontent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 10\CathodeRayTube.txt"
for($lineIdx = 0; $lineIdx -lt $filecontent.Length; $lineIdx++)
{
    $linecontent = $filecontent[$lineIdx]
    $pair = $linecontent.Split(' ')
    if($pair[0] -eq 'addx')
    {
        if($cycles -eq 40)
        {
            $cycles = 0
        }
        $crtrows += $spritecurrentwindow[$cycles++]
        if($cycles -eq 40)
        {
            $cycles = 0
        }
        $crtrows += $spritecurrentwindow[$cycles++]
        if([int]$pair[1] -gt 0)
        {
            $spritewindowstartpos -= $pair[1]
        }
        else
        {
            $spritewindowstartpos += [math]::Abs($pair[1])
        }
        $spritecurrentwindow = $spritestaticwindow.Substring($spritewindowstartpos, 40)
    }
    else
    {#noop        if($cycles -eq 40)
        {
            $cycles = 0
        }
        $crtrows += $spritecurrentwindow[$cycles++]
    }
  # Write-Host $crtrows
  # Write-Host $spritecurrentwindow
}

for($i = 0; $i -lt $crtrows.Length; $i++)
{
    $crtrow += $crtrows[$i]
    if(($i -eq 39) -or ($i -eq 79) -or ($i -eq 119) -or ($i -eq 159) -or ($i -eq 199) -or ($i -eq 239))
    {
        Write-Host $crtrow
        $crtrow = ''
    }
}
