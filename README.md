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
