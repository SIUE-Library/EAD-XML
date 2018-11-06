./makeTsv.sh; for each in `ls -d */. | cut -f1 -d/ `; do ./loadTsv.sh $each > "$each.txt"; done
