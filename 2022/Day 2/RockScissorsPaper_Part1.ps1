$possibleStrategies = @{
    'A X' = 4 #rock - rock
    'A Y' = 8 #rock - paper
    'A Z' = 3 #rock - scissors
    'B X' = 1 #paper - rock
    'B Y' = 5 #paper - paper
    'B Z' = 9 #paper - scissors
    'C X' = 7 #scissors - rock
    'C Y' = 2 #scissors - paper
    'C Z' = 6 #scissors - scissors
}
[int]$totalscore = 0
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 2\strategy.txt" | ForEach-Object{
    if($possibleStrategies.ContainsKey($_))
    {
        $totalscore += $possibleStrategies[$_]
    }
    else
    {
        Write-Host "Not covered strategy - " + $_
        pause
    }
}
Write-Host "Total score is: "$totalscore