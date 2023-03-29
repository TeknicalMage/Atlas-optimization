

$a = {Write-Output $line}

$b = {python Split.py -f $Line;}

foreach($line in Get-Content .\urllist.txt) {
    if($line -match $regex){
        
     
        $path = 'H:\Projects\Atlas-optimization'
        $file = 'Split.py'
        $cmd = $path+"\\"+$file

        Start-Process $cmd

    }

}