$decryptedstrategies = @{
    'A X' = 'A Z' #need to loose
    'A Y' = 'A X' #need to draw
    'A Z' = 'A Y' #need to win
    'B X' = 'B X' #need to loose
    'B Y' = 'B Y' #need to draw
    'B Z' = 'B Z' #need to win
    'C X' = 'C Y' #need to loose
    'C Y' = 'C Z' #need to draw
    'C Z' = 'C X' #need to win
}
$newStrategyFilePath = "c:\Users\usr\Documents\Advent Of Code\2022\Day 2\decryptedstrategy.txt"
Get-Content -Path "c:\Users\usr\Documents\Advent Of Code\2022\Day 2\strategy.txt" | ForEach-Object{
    if($decryptedstrategies.ContainsKey($_))
    {
        Add-Content -Path $newStrategyFilePath -Value $decryptedstrategies[$_]
    }
    else
    {
        Write-Host "Not decrypted strategy - " + $_
        pause
    }
}

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
Get-Content -Path $newStrategyFilePath | ForEach-Object{
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