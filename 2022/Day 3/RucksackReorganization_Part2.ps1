$itemtypepriorities = New-Object hashtable
$itemtypepriorities.a = 1
$itemtypepriorities.b = 2
$itemtypepriorities.c = 3
$itemtypepriorities.d = 4
$itemtypepriorities.e = 5
$itemtypepriorities.f = 6
$itemtypepriorities.g = 7
$itemtypepriorities.h = 8
$itemtypepriorities.i = 9
$itemtypepriorities.j = 10
$itemtypepriorities.k = 11
$itemtypepriorities.l = 12
$itemtypepriorities.m = 13
$itemtypepriorities.n = 14
$itemtypepriorities.o = 15
$itemtypepriorities.p = 16
$itemtypepriorities.q = 17
$itemtypepriorities.r = 18
$itemtypepriorities.s = 19
$itemtypepriorities.t = 20
$itemtypepriorities.u = 21
$itemtypepriorities.v = 22
$itemtypepriorities.w = 23
$itemtypepriorities.x = 24
$itemtypepriorities.y = 25
$itemtypepriorities.z = 26

[int]$prioritiessum = 0
$elfgroup = 0
$filelines = Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 3\AllRucksacksContent.txt"
for($filelineidx = 0; $filelineidx -lt ($filelines.Count - 2); $filelineidx += 3)
{
    $commonitemtypefound = $false
    $elfgroup++
    $firstelfrucksack = $filelines[$filelineidx]
    $secondelfrucksack = $filelines[$filelineidx+1]
    $thirdelfrucksack = $filelines[$filelineidx+2]

    foreach($character in $firstelfrucksack.ToCharArray())
    {
        if(($secondelfrucksack.IndexOf($character) -ne -1) -and ($thirdelfrucksack.IndexOf($character) -ne -1))
        {
            if($itemtypepriorities.ContainsKey($character.ToString()))
            {
                $itemtypepriority = $itemtypepriorities[$character.ToString()]
            }
            else
            {   
                $itemtypepriority = $itemtypepriorities[$character.ToString().ToLower()] + 26
            }
            Write-Host $elfgroup ":" $character "=" $itemtypepriority
            $prioritiessum += $itemtypepriority
            $commonitemtypefound = $true
            break
        }
    }
    if(!$commonitemtypefound)
    {
        Write-Host "No common item type for folowing group of elf's rucksacks:" $firstelfrucksack "-" $secondelfrucksack "-" $thirdelfrucksack
    }
}
Write-Host "The sum of the priorities of item types is: "$prioritiessum
Pause