#!/bin/bash
for file in rawData/*.txt
do
    if ! [ -s $file ]
    then
	filename=$(basename -- "$file")
	verb=${filename%.*}
	echo $verb
	chromium-browser http://www.spanishdict.com/conjugate/$verb
	sleep 5
	xdotool key Tab
	xdotool key Ctrl+a
	xdotool key Ctrl+c
	xdotool key Ctrl+w
	sleep 5
	xsel -b > rawData/$verb.txt
	sleep 1
	python convertPageToJS.py rawData/$verb.txt
    fi
done
