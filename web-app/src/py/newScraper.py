import requests
import json
import os
from bs4 import BeautifulSoup
from time import sleep

# change dir to py folder

f = open("list.txt", "r")
fi = open("groups.json", "a", encoding="utf-8")

base = "https://steamcommunity.com/groups/"


for i in f:
    url = base + i.strip()
    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")

    # check if group exists
    if "An error was encountered while processing your request" in x.text:
        continue
    if soup == None:
        continue

    # get groupname and tag
    groupName = soup.find("title").text[28:]
    # delete quotes in group name if exist, they screw up json
    
    groupTag = soup.find("span", class_="grouppage_header_abbrev")
    if groupTag is not None:
        groupTag = groupTag.text
    else:
        continue

    # check if private
    if "Request To Join" in x.text or "Membership by invitation only" in x.text:
        private = True
    else:
        private = False

    # print formatted with : for json
    out = '\t{\n\t\t"GroupName": ' + json.dumps(groupName) + ',\n\t\t"GroupTag": ' + json.dumps(groupTag) + ',\n\t\t"GroupUrl": ' + json.dumps(url) + ',\n\t\t"IsPrivate": ' + json.dumps(private) + "\n\t},\n"
    fi.write(out)

    # print just for debug stuff
    print("printing: " + groupTag)
    sleep(0.25)


f.close()
fi.close()