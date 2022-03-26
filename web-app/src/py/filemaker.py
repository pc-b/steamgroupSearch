dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_']

f = open("list.txt", "w+")

for i in range(0, len(dict)):
    for j in range(0, len(dict)):
        for k in range(0, len(dict)):
            f.write(dict[i] + dict[j] + dict[k] + "\n")

f.close()