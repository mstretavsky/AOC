function Get-VisibleTrees([array]$treesarray)
{
    [Int32[]]$visibletrees = @(0)
    $highesttree = $treesarray[0]
    $highesttreeidx = 0
    for($forwardidx=1; $forwardidx -lt $treesarray.Length;$forwardidx++)
    {
        if($highesttree -gt $treesarray[$forwardidx])
        {
            continue
        }
        elseif($highesttree -lt $treesarray[$forwardidx])
        {
            $visibletrees += $forwardidx
            $highesttreeidx = $forwardidx
        }
        $highesttree = $treesarray[$forwardidx]
    }
    $visibletrees += $treesarray.Length-1
    if($highesttreeidx -eq ($treesarray.Length-1))
    {
        return $visibletrees
    }
    $highesttree = $treesarray[$treesarray.Length-1]
    for($backwardidx = $treesarray.Length-2; $backwardidx -gt $highesttreeidx; $backwardidx--)
    {
        if($highesttree -ge $treesarray[$backwardidx])
        {
            continue
        }
        $highesttree = $treesarray[$backwardidx]
        $visibletrees += $backwardidx
    }
    return $visibletrees
}
$fileContent = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 8\TreetopTreehouse.txt"
[int32[][]]$alltreesmatrix = new-object int32[][] $fileContent.Count,$fileContent.Count

for($lineIdx = 1; $lineIdx -lt $fileContent.Length-1; $lineIdx++)
{
    $visibletreesindexes = Get-VisibleTrees($fileContent[$lineIdx].ToCharArray())
    foreach($index in $visibletreesindexes)
    {
        $alltreesmatrix[$lineIdx][$index] = 1
    }
}
for($colidx = 1; $colidx -lt $fileContent[0].Length-1; $colidx++)
{
    $array = @()
    for($lineIdx = 0; $lineIdx -lt $fileContent.Length; $lineIdx++)
    {
        $array += $fileContent[$lineIdx][$colidx]
    }
   $visibletreesindexes = Get-VisibleTrees($array)
   foreach($index in $visibletreesindexes)
   {
        $alltreesmatrix[$index][$colidx] = 1    
   }
}
$alltrees = 4
foreach($matrixline in $alltreesmatrix)
{
    Write-Host $matrixline
    foreach($matrixlineitem in $matrixline)
    {
        $alltrees += $matrixlineitem
    }
}
Write-Host $alltrees
