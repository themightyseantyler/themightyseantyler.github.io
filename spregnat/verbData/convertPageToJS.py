import sys, os, re
from pprint import pprint


def getVerbDictionary(inputFile):
    verb = {}
    voices = ["Indicative", "Subjunctive", "Imperative", "Perfect", "Continuous (Progressive)", "Perfect Subjunctive"]
    voice = ""
    persons = ["yo", "tú", "Ud.", "nosotros", "vosotros", "Uds."]
    person = ""
    tenseCount = 99
    tenses = []
    with open(inputFile, "r") as input:
        for line in input:
            check = line.strip()
            if check in voices:
                voice = check
                verb[voice] = {}
            if voice != "":
                if "Present" in line:
                    tenses = [t.strip() for t in line.split("\t")]
                    for tense in tenses:
                        verb[voice][tense] = {}
                elif "Affirmative" in line:
                    tenses = [t.strip() for t in line.split()]
                    for tense in tenses:
                        verb[voice][tense] = {}
       
            if check.endswith("Uds."):
                personCheck = line.strip()[-4:]
            elif check.endswith("os"):
                personCheck = line.strip()
            else:
                personCheck = line.strip()[-3:]
            if personCheck in persons:
                tenseCount = -1
                person = personCheck
                for tense in tenses:
                    verb[voice][tense][person] = ""
                
            if voice != "" and len(tenses) > 0 and person != "" and tenseCount < len(tenses):
                try:
                    verb[voice][tenses[tenseCount]][person] = line.strip()
                    tenseCount += 1
                except:
                    if tenseCount == -1:
                        tenseCount += 1
                    #print(voice,tenses, person)
                    #print(tenseCount)
                    #exit()
            if line == "\n":
                voice = ""
    return verb


def saveDictToFile(inFilename):
    verbName = inFilename.split(".")[0].split("/")[-1]
    outFilename = "verbObjectFiles" + os.sep + verbName + ".js"
    verbDict = getVerbDictionary(inFilename)
    with open(outFilename, "w") as outfile:
        outfile.write("var " + verbName + " = {\n")
        for key in verbDict.keys():
            outfile.write("\t" + re.sub('[\s+()]', '',key) + ": {\n")
            for key2 in verbDict[key].keys():
                outfile.write("\t\t" + re.sub('[\s+()]', '',key2) + ": {\n")
                for key3 in verbDict[key][key2].keys():
                    outfile.write('\t\t\t' + re.sub('[\s+.]', '',key3) + ': "' +
                                  verbDict[key][key2][key3]
                                  + '",\n')
                outfile.write("\t\t},\n")
            outfile.write("\t},\n")
        outfile.write("}\n")

def main():
    inputFilename = sys.argv[1]
    saveDictToFile(inputFilename)

if __name__ == "__main__":
    main()
