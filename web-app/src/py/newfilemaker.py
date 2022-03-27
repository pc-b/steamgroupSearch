import os
os.chdir("./web-app/src/py")

f = open("old_list.txt", "r", encoding="utf-8")
fi = open("words_alpha.txt", "r")
fil = open("list.txt", "a", encoding="utf-8")


for i in fi:
    i = i.strip()
    if i not in f:
        fil.write(i.strip() + "\n")

f.close()
fi.close()
fil.close()