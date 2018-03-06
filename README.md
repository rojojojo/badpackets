# badpackets
Python script to automate lookups on Mirai-like Bad Packets 

You can use this tool to look up an IP address & check if it is part of mirai-like botnet. You can also provide a text file with a list of IP addresses (one per line). By default the script shows the most recent entries. Source of data is mirai.badpackets.net.  


Install dependencis using the following command:  
pip install -r requirements.txt  

usage:  
usage: badpackets.py [-h] [-i IPADDRESS] [-f FILENAME]  


  -h, --help    show this help message and exit  
  -i IPADDRESS  IP Address to be checked  
  -f FILENAME   Text file with the list of IP Addresses  

Example outputs:  
1. python badpackets.py  

Looking up on Badpackets...  
Most recent entries...  
---------------------  
IP Address: 113.238.139.120  
Country Code: CN  
Autonomous System Name: CHINA169-BACKBONE CHINA UNICOM China169 Backbone  
First Seen: 2018-03-04 23:48:28 PST  
---------------------  
  
  
2. python badpackets.py -i 202.220.247.57  
Looking up on Badpackets...  
---------------------  
IP Address: 202.220.247.57  
Country Code: JP  
Autonomous System Name: ACCSNET Academic newtown Community Cable Service  
First Seen: 2018-03-04 23:10:08 PST  
---------------------  
  

Feedback welcome!
