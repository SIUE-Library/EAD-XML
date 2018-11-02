rm "$1.txt"; for file in $1/*.tsv; do \cp -rf $file html.tsv; python3 getFirstWord.py $1; done; python3 removeHeaders.py $1; 
 cat "$1.txt" ;
