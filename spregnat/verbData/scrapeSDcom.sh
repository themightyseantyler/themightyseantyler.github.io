#!/bin/bash
filename="verbList.txt"
while IFS= read -r verb
do
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
done <$filename

