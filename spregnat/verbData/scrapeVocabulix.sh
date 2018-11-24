#!/bin/bash
urlSuffix="_spanish.html"
declare -a prefixes=("a" "a1" "a2" "b" "c" "c1" "d" "d1" "e" "e1" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "p1" "q" "r" "r1" "s" "t" "u" "v" "w" "x" "y" "z")
for i in "${prefixes[@]}"
do
    url="https://www.vocabulix.com/conjugacion2/"$i$urlSuffix
    echo $url
    chromium-browser $url
    sleep 5
    xdotool key Ctrl+a
    xdotool key Ctrl+c
    xdotool key Ctrl+w
    sleep 5
    xsel -b >> verbDataRaw.txt
done

python cleanVerbList.py verbDataRaw.txt
