#Shell to run bilingual-sentence-aligner on all parallel/SentPerLine/English/Ei_* and Hindi/Hi_*
#Hardcoded: sentence number 1 to 62

file_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine'
efile_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine/English'
hfile_dir='/home/kishori/ILP_isha/codes/parallel/SentPerLine/Hindi'

i=1
while [ $i -lt 62 ]
do

efile=`ls $efile_dir/E"$i"_*.txt`
hfile=`ls $hfile_dir/H"$i"_*.txt`
#echo $efile

perl align-sents-all.pl $efile $hfile

newdirname=EH$i

if [ -d "$file_dir"/"$newdirname" ]; then
echo "^^^^^^^^^^^^ $newdirname" already exists;

else
`mkdir "$file_dir"/$newdirname`;
echo "$newdirname" created;
fi

cp $efile "$file_dir"/$newdirname
cp $hfile "$file_dir"/$newdirname

ealignfile=`ls $efile_dir/E"$i"_*.aligned`
mv $ealignfile  $file_dir/$newdirname
elb=`ls $efile_dir/E"$i"_*.length-backtrace`
mv $elb  $file_dir/$newdirname
eb=`ls $efile_dir/E"$i"_*.backtrace`
mv $eb  $file_dir/$newdirname
emp=`ls $efile_dir/E"$i"_*.model-one`
mv $emp  $file_dir/$newdirname
esn=`ls $efile_dir/E"$i"_*.search-nodes`
mv $esn  $file_dir/$newdirname
ewords=`ls $efile_dir/E"$i"_*.words`
mv $ewords  $file_dir/$newdirname
etrain=`ls $efile_dir/E"$i"_*.train`
mv $etrain  $file_dir/$newdirname

halignfile=`ls $hfile_dir/H"$i"_*.aligned`
mv $halignfile  $file_dir/$newdirname
hwords=`ls $hfile_dir/H"$i"_*.words`
mv $hwords  $file_dir/$newdirname
htrain=`ls $hfile_dir/H"$i"_*.train`
mv $htrain  $file_dir/$newdirname
((i=i+1))

echo "******************************************************************"
done
