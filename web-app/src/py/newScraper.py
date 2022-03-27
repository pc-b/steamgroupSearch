import requests
import json
import os
from bs4 import BeautifulSoup
from time import sleep

# change dir to py folder
#os.chdir("./web-app/src/py")

f = open("list.txt", "r")
fi = open("groups.txt", "a", encoding="utf-8")

base = "https://steamcommunity.com/groups/"



for i in f:
    url = base + i.strip()
    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")

    # check if group exists
    if "An error was encountered while processing your request" in x.text:
        continue

    # get groupname and tag
    groupName = soup.find("title").text[28:]
    # delete quotes in group name if exist, they screw up json
    groupTag = soup.find("span", class_="grouppage_header_abbrev").text

    # check if private
    if "Request To Join" in x.text or "Membership by invitation only" in x.text:
        private = True
    else:
        private = False

    # print formatted with : for json
    out = "GroupName:" + groupName + " 💚 " + "GroupTag:" + groupTag + " 💚 " + "GroupURL:" + url + " 💚 " + "IsPrivate:" + str(private) + "\n"
    fi.write(out)

    # print just for debug stuff
    print("printing: " + groupTag)


f.close()
fi.close()