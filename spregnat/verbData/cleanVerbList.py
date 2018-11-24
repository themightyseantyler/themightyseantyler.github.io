import sys, os
rawList = sys.argv[1]
verbs = []
with open(rawList, "r") as rawData:
    for rawline in rawData:
        line = rawline.strip()
        if line.endswith("ir") or line.endswith("er") or line.endswith("ar"):
            if " " not in line:
                verbs.append(line)
with open("verbList.txt", "w") as outfile:
    for verb in verbs:
        outfile.write(verb+"\n")
