import sys, os
verbList = sys.argv[1]
if "-" in verbList:
    freqNumber = "-"+verbList.split("-")[-1].split(".")[0]
else:
    freqNumber = ""
outputFileName = "verbObjectFiles/zz_list"+freqNumber+".js"
with open(verbList, "r") as verbListFile:
    with open(outputFileName, "w") as outfile:
        outfile.write('var verbs = [\n')
        for line in verbListFile:
            outfile.write('\t"'+line.strip()+'",\n')
        outfile.write(']')

