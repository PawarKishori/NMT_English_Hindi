out_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine/champollion_out'
file_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine'
efile_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine/English'
hfile_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine/Hindi'

MYPATH=`pwd`
export CTK=$MYPATH/champollion-1.2
echo "Champollion is in: "$CTK

#echo "------------------------"i
#basename $CTK
#file=`basename $CTK`
#echo $file
#echo "------------------------"i

i=244
while [ $i -lt 361 ]
do

	echo "value of i is" $i
	echo
	echo "------------------------"$i
	efilepath=`ls $efile_dir/E"$i"_*.txt`
	hfilepath=`ls $hfile_dir/H"$i"_*.txt`

	echo "Input1: " $efilepath
	echo "Output1: "$hfilepath	

	efilename=`basename $efilepath`
	echo "Outfilename: "$efilename
	
	out_file=$out_dir/"$efilename"_align_id.txt
	
	

	$CTK/bin/champollion.EH $efilepath $hfilepath  $out_file
	echo "OutFile created:  " $out_file
	echo


	
	
	python convert_champ_out.py $out_dir/$efilename"_align_id.txt" $efilepath $hfilepath $out_dir/$efilename"_align_sent.txt"
	paste $out_dir/$efilename"_align_sent.txt" $out_dir/$efilename"_align_id.txt" > $out_dir/$efilename
	mv $out_dir/$efilename `echo $out_dir/$efilename | sed 's/\(.*\.\)txt/\1xlsx/'`
	#echo 
	
	i=$((i+1))
	echo "------------------------"$i
done
