import os

os.chdir("./web-app/src/py")

lines_seen = set() # holds lines already seen
outfile = open("list2.txt", "w")
for line in open("new_list.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()