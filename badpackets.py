#! python3
# Author: rojojojo (Rohan)
# badpackets.py - Python script to automate lookups on Mirai-like Bad Packets.

import requests
import argparse
import bs4

parser = argparse.ArgumentParser(description="Python script to automate lookups on Mirai-like Bad Packets. You can use this "
                                             "tool to look up an IP address & check if it is part of mirai-like botnet. "
                                             "You can also provide a text file with a list of IP addresses "
                                             "(one per line). By default the script shows the most recent entries. "
                                             "Source of data is mirai.badpackets.net.")
parser.add_argument("-i", dest='ipAddress', help='IP Address to be checked')
parser.add_argument("-f", dest='filename', help="Text file with the list of IP Addresses")
args = parser.parse_args()

ipAddress = str(args.ipAddress)
filename = str(args.filename)


def badpackets(ipaddr):
    res = requests.get('https://mirai.badpackets.net/?ipAddress=' + ipaddr)
    res.raise_for_status()
    wiki = bs4.BeautifulSoup(res.text, "html.parser")
    wiki_address = wiki.select('table.table.table-override tbody td.ipAddress')
    wiki_countrycode = wiki.select('table.table.table-override tbody td.country')
    wiki_autonomous = wiki.select('table.table.table-override tbody td.autonomousSystem')
    wiki_seen = wiki.select('table.table.table-override tbody td.firstSeen')
    print('---------------------')
    print('IP Address: ' + wiki_address[0].getText())
    print('Country Code: ' + wiki_countrycode[0].getText())
    print('Autonomous System Name: ' + wiki_autonomous[0].getText())
    print('First Seen: ' + wiki_seen[0].getText())
    print('---------------------')


def badpackets_top():
    res = requests.get('https://mirai.badpackets.net/?sort=-firstSeen')
    res.raise_for_status()
    wiki = bs4.BeautifulSoup(res.text, "html.parser")
    wiki_address = wiki.select('table.table.table-override tbody td.ipAddress')
    wiki_countrycode = wiki.select('table.table.table-override tbody td.country')
    wiki_autonomous = wiki.select('table.table.table-override tbody td.autonomousSystem')
    wiki_seen = wiki.select('table.table.table-override tbody td.firstSeen')
    for i in range(25):
        print('---------------------')
        print('IP Address: ' + wiki_address[i].getText())
        print('Country Code: ' + wiki_countrycode[i].getText())
        print('Autonomous System Name: ' + wiki_autonomous[i].getText())
        print('First Seen: ' + wiki_seen[i].getText())
        print('---------------------')


if ipAddress != "None":
    print('Looking up on Badpackets...') # display text while downloading the Badpackets page
    badpackets(ipAddress)

elif filename != "None":
    print('Looking up on Badpackets...')  # display text while downloading the Badpackets page
    temp_file = open(filename)
    for l in temp_file:
        ip_addr = l.strip('\n')
        badpackets(ip_addr)
else:
    print('Looking up on Badpackets...')  # display text while downloading the Badpackets page
    print('Most recent entries...')
    badpackets_top()