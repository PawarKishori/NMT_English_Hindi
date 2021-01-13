###Code for *.docx
#for file in *.docx; 
#  #do catdoc $file > $file'.txt' #for *.doc 
#  do  docx2txt $file       
#done

###Code for *.doc
for file in *.doc
  do 
echo $file
catdoc $file  > $file'.txt'
done
