import os, sys
from operator import itemgetter
from pprint import pprint
frequencyListFile = sys.argv[1]
vocabListFile = sys.argv[2]
verbs = []
frequentVerbs = []
with open(vocabListFile, "r") as verbList:
    for entry in verbList:
        verbs.append(entry.strip())
with open(frequencyListFile, "r") as frequencyList:
    count = 0
    for index, line in enumerate(frequencyList):
        word = line.split(" ")[0].strip()
        #frequency = line.split(" ")[0].strip()
        if word in verbs:
            frequentVerbs.append((word, index))
        if len(frequentVerbs) == 250:
            break
frequentVerbs.sort(key=itemgetter(1))
top250Verbs = [verb[0] for verb in frequentVerbs]
with open("verbList-50.txt", "w") as list50:
    with open("verbList-100.txt", "w") as list100:
        with open("verbList-250.txt", "w") as list250:
            for iVerb, verb in enumerate(top250Verbs):
                if iVerb < 50:
                    list50.write(verb+"\n")
                    list100.write(verb+"\n")
                    list250.write(verb+"\n")
                elif iVerb < 50:
                    list100.write(verb+"\n")
                    list250.write(verb+"\n")
                else:
                    list250.write(verb+"\n")
