##RUN:
##	sh run_champ.sh ENG HND 
##OUTPUT:	ENG_final_align.txt
##NOTE:	Inputs should be one sentence per line. (Both ENG and HND)


MYPATH=`pwd`
export CTK=$MYPATH/champollion-1.2
echo "Champollion is in: "$CTK

$CTK/bin/champollion.EH $1 $2  $1_align_id.txt

python convert_champ_out.py  $1_align_id.txt  $1 $2 $1_align_sent.txt
#$MYPATH/align-eng-hnd.out $1_align.txt hnd  eng  $1_final_align.txt
