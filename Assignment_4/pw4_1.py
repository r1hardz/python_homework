import os
os.chdir(os.path.dirname(__file__))

filename = input("Enter filename: ")
with open(filename, "r") as f:
    senderList = []
    for line in f:
        if (line.startswith("From") and not line.startswith("From:")):
            senderList.append(line.split()[1])
    print(*sorted(senderList), sep="\n")
    print("There were", len(senderList), "lines in the file with From as the first word")
    f.close()
