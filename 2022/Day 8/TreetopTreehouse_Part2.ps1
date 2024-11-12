function Get-ScenicScore([array]$treesarray, $idx)
{
    if(($idx -eq 0) -or ($idx -eq $treesarray.Length-1))
    {
        pause
    }

    $leftsidescenicscore = 0
    $treeheight = $treesarray[$idx]
    for($i = $idx-1; $i -ge 0; $i--)
    {
        $lefttreeheight = $treesarray[$i]
        if($lefttreeheight -lt $treeheight)
        {
            $leftsidescenicscore++
        }
        else
        {
            $leftsidescenicscore++
            break
        }
    }
    $rightsidescenicscore = 0
    for($i = $idx+1; $i -lt $treesarray.Length; $i++)
    {
        $righttreeheight = $treesarray[$i]
        if($righttreeheight -lt $treeheight)
        {
            $rightsidescenicscore++
        }
        else
        {
            $rightsidescenicscore++
            break
        }
    }
    return ($leftsidescenicscore*$rightsidescenicscore)
}
$fileContent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 8\TreetopTreehouse.txt"
[int32[][]]$alltreesmatrix = new-object int32[][] $fileContent.Count,$fileContent.Count

$maxscenicscore = 0
$position = ''
for($lineIdx = 1; $lineIdx -lt $fileContent.Length-1; $lineIdx++)
{
    for($colidx = 1; $colidx -lt $fileContent.Length-1; $colidx++)
    {
        $scenicscore = Get-ScenicScore -treesarray $fileContent[$lineIdx].ToCharArray() -idx $colidx
        $array = @()
        for($j = 0; $j -lt $fileContent.Length; $j++)
        {
            $array += $fileContent[$j][$colidx]
        }
        $scenicscore *= Get-ScenicScore -treesarray $array -idx $lineIdx

        if($scenicscore -gt $maxscenicscore)
        {
            $maxscenicscore = $scenicscore
            $position = ''+$lineIdx+':'+ $colidx+''
        }
    }

}

Write-Host $maxscenicscore
Write-Host $position
