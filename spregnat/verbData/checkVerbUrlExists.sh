#!/bin/bash
rm verbList.txt
filename="verbList-all.txt"
searchTerm="Showing results for"
while IFS= read -r verb
      do
	  if ! grep -q "$searchTerm" rawData/$verb.txt
	  then
	      echo $verb >> verbList.txt
	  fi
done <$filename



