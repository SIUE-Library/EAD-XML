rm out.txt; for file in $1/*.tsv; do \cp -rf $file html.tsv; python getFirstWord.py; done; python removeHeaders.py; 
 cat out.txt ;
