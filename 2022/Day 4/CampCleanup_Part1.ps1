$numvalidpairs = 0
$numoveralpedsections = 0
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 4\CampCleanup.txt" | ForEach-Object{
    $sections = $_.Split(',')
    
    $startidx1 = $sections[0].Split('-')[0]
    $endidx1 = $sections[0].Split('-')[1]
    $startidx2 = $sections[1].Split('-')[0]
    $endidx2 = $sections[1].Split('-')[1]

    [string]$fullSections_1 = ''
    for([int]$idx = $startidx1; $idx -le $endidx1; $idx++)
    {
        $fullSections_1 += ','
        $fullSections_1 += $idx.ToString()
        $fullSections_1 += ','
    }

    [string]$fullSections_2 = ''
    for($idx = $startidx2; $idx -le $endidx2; $idx++)
    {
        $fullSections_2 += ','
        $fullSections_2 += $idx.ToString()
        $fullSections_2 += ','
    }

    if($fullSections_2.Contains($fullSections_1) -or $fullSections_1.Contains($fullSections_2))
    {
        Write-Host $sections[0]','$sections[1]
        $numvalidpairs++
    }
    else
    {
        $fullSections_1 = $fullSections_1.TrimStart(',')
        $fullSections_1 = $fullSections_1.TrimEnd(',')
        $partlySections_1 = $fullSections_1.Split(',,', [StringSplitOptions]::RemoveEmptyEntries)
        for($idx = 0; $idx -lt $partlySections_1.Count; $idx++)
        {
            $numberwithcomma = ''
            $numberwithcomma += ','
            $numberwithcomma += $partlySections_1[$idx]
            $numberwithcomma += ','
            if($fullSections_2.Contains($numberwithcomma))
            {
                Write-Host $sections[0]','$sections[1]
                $numoveralpedsections++
                break
            }
        }
    }
}
$numoveralpedsections += $numvalidpairs
Write-Host "The number of pairs containing each other: "$numvalidpairs
Write-Host "The number of pairs overlaping each other: "$numoveralpedsections
Pause