
$monkeysinspections = @(0, 0, 0, 0, 0, 0, 0, 0)
$monkeysitems = New-Object -TypeName System.Collections.ArrayList
$monkeysitems.Add(@(71,85))
$monkeysitems.Add(@(66, 50, 90, 53, 88, 85))
$monkeysitems.Add(@(97, 54, 89, 62, 84, 80, 63))
$monkeysitems.Add(@(82, 97, 56, 92))
$monkeysitems.Add(@(50, 99, 67, 61, 86))
$monkeysitems.Add(@(61, 66, 72, 55, 64, 53, 72, 63))
$monkeysitems.Add(@(59, 79, 63))
$monkeysitems.Add(@(55))

function ComputeMonkey0($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item * 13
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 19, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(6) | Out-Null
        }
        else 
        {
            $monkey_item.Add(7) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey1($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item + 3
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 2, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(5) | Out-Null
        }
        else 
        {
            $monkey_item.Add(4) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey2($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item + 6
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 13, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(4) | Out-Null
        }
        else 
        {
            $monkey_item.Add(1) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey3($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item + 2
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 5, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(6) | Out-Null
        }
        else 
        {
            $monkey_item.Add(0) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey4($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item * $item
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 7, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(5) | Out-Null
        }
        else 
        {
            $monkey_item.Add(3) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey5($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item + 4
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 11, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(3) | Out-Null
        }
        else 
        {
            $monkey_item.Add(0) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey6($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item * 7
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 17, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(2) | Out-Null
        }
        else 
        {
            $monkey_item.Add(7) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
function ComputeMonkey7($items)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    foreach($item in $items.GetEnumerator())
    {
        $monkey_item = New-Object -TypeName System.Collections.ArrayList
        [int]$newitem = $item + 7
        $newitem /= 3
        $monkey_item.Add($newitem) | Out-Null
        $divresult = 0
        [math]::DivRem($newitem, 3, [ref]$divresult) | Out-Null
        if($divresult -eq 0)
        {
            $monkey_item.Add(2) | Out-Null
        }
        else 
        {
            $monkey_item.Add(1) | Out-Null
        }
        $thrownitems.Add($monkey_item) | Out-Null
    }
    return $thrownitems
}
for($i = 0; $i -lt 20; $i++)
{
    $thrownitems = New-Object -TypeName System.Collections.ArrayList
    $thrownitems = ComputeMonkey0($monkeysitems[0])
    $monkeysinspections[0] += $monkeysitems[0].Count
    $monkeysitems[0].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += $item[0]
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey1($monkeysitems[1])
    $monkeysinspections[1] += $monkeysitems[1].Count
    $monkeysitems[1].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey2($monkeysitems[2])
    $monkeysinspections[2] += $monkeysitems[2].Count
    $monkeysitems[2].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey3($monkeysitems[3])
    $monkeysinspections[3] += $monkeysitems[3].Count
    $monkeysitems[3].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey4($monkeysitems[4])
    $monkeysinspections[4] += $monkeysitems[4].Count
    $monkeysitems[4].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey5($monkeysitems[5])
    $monkeysinspections[5] += $monkeysitems[5].Count
    $monkeysitems[5].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey6($monkeysitems[6])
    $monkeysinspections[6] += $monkeysitems[6].Count
    $monkeysitems[6].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
    $thrownitems.Clear()
    $thrownitems = ComputeMonkey7($monkeysitems[7])
    $monkeysinspections[7] += $monkeysitems[7].Count
    $monkeysitems[7].Clear()
    foreach($item in $thrownitems)
    {
        $monkeysitems[$item[1]] += ($item[0])
    }
}

$monkeysinspections | Sort-Object

Write-Host $monkeysinspections[0] * $monkeysinspections[1]