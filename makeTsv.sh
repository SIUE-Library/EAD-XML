
for file in */*.pdf
do
	echo "$file";
	convert -density 400 $file "$file.png";
done;

for file in */*.png
do
	echo $file;
	tesseract $file $file -oem 2 tsv -c tosp_min_sane_kn_sp=1
done;
