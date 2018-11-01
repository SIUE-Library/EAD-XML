rm out.txt; for file in $1/*.tsv; do \cp -rf $file html.tsv; python3 getFirstWord.py; done; python3 removeHeaders.py; 
 cat out.txt ;
