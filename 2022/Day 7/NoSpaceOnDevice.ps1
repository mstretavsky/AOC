$filesystemmap = New-Object -TypeName System.Collections.Hashtable
$parentkey = 'parent\'
$filesystemmap.Add($parentkey, 0)
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 7\NoSpaceOnDevice.txt" | ForEach-Object{
    if($_.Contains('$ cd /') -or $_.Contains('$ ls'))
    {
        return
    }
    if($_.Contains('$ cd '))
    {
        $cdcommand = $_.Substring(5, $_.Length - 5)
        if($cdcommand -eq '..')
        {
            $parentkey = $parentkey.TrimEnd('\')
            $parentkey = $parentkey.Remove($parentkey.LastIndexOf('\'))
            $parentkey += '\'
        }
        else
        {
            $parentkey = $parentkey + $cdcommand + '\'
            if(!$filesystemmap.ContainsKey($parentkey))
            {
                Write-Host "Missing key:"$parentkey
            }
        }
    }
    elseif($_.Contains('dir '))
    {
        $dirname = $_.Substring(4, $_.Length - 4)
        $newkey = $parentkey + $dirname + '\'
        $filesystemmap.Add($newkey, 0)
    }
    else
    {
        $value = $_.Split(' ')[0]
        foreach($mapkey in @($filesystemmap.Keys))
        {
            if($parentkey.Contains($mapkey))
            {
                $filesystemmap[$mapkey] += $value
            }
        }
    }
}
$totalSize = 0
foreach($hashmapvalue in $filesystemmap.Values)
{
    if($hashmapvalue -le 100000)
    {
        $totalSize += $hashmapvalue
    }
}
Write-Host $totalSize

#part II
$overallunusedspace = 70000000 - $filesystemmap['parent\']
$amoutneededtorelease = 30000000 - $overallunusedspace
$closerfilefolderamount = 70000000
$closerfilefolder = ''
foreach($hashmapitem in $filesystemmap.GetEnumerator())
{
    $difference = $hashmapitem.value - $amoutneededtorelease
    if(($difference -ge 0) -and ($difference -lt $closerfilefolderamount))
    {
        $closerfilefolderamount = $difference
        $closerfilefolder = $hashmapitem.Key
    }
}
Write-Host $filesystemmap[$closerfilefolder]

