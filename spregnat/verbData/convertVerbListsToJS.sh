#!/bin/bash
rm ../js/verbList*
declare -a filenames=("verbList" "verbList-50" "verbList-100" "verbList-250")
for file in "${filenames[@]}"
do
    filename=$file.txt
    python createVerbListJS.py $filename
    while IFS= read -r verb
    do
	cat verbObjectFiles/$verb.js >> ../js/$file.js
    done <$filename
done

for i in 50 100 250
do
    cat verbObjectFiles/zz_list-$i.js >> ../js/verbList-$i.js
done

cat verbObjectFiles/zz_list.js >> ../js/verbList.js
