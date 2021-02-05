##RUN:
##	sh run_sentence_alignment.sh ENG HND 
##OUTPUT:	ENG_final_align.txt
##NOTE:	Inputs should be one sentence per line. (Both ENG and HND)


MYPATH=`pwd`
export CTK=$MYPATH/champollion-1.2
echo "Champollion is in: "$CTK

$CTK/bin/champollion.EH $1 $2  $1_align.txt

$MYPATH/align-eng-hnd.out $1_align.txt hnd  eng  $1_final_align.txt
