1. ProcessXls-1.py: 
	First program to be run on the xls, provided by the volunteer.

	Input xls should be in below format:
	column1		
	1) Questioner: Today is my birthday. <=> 1] Questioner: [text in hindi font]
	column2: 1 <=> 1
	column3: 1

	Output xls
	column1		
	1) Questioner: Today is my birthday. <=> 1] Questioner: [text in hindi font]
	column2: 1 <=> 1
	column3: 1
	column4:
	1) Questioner: Today is my birthday. <=> 1] Questioner: [text in hindi font]
	column5:
	ERROR (non mandatory)
--------------------------------------------

2. CreateHindiEnglishTextFile-2.py: 
	Second program to be run on the xls output from first program

	Creates test files in hindi and english eg: E112_hindi_aligned.txt and E112_eng_aligned.txt
--------------------------------------------

3. CreateTestTrainDataset-3.py: 
	Third program to be run on the output from second program

	Input: Folder where the input txt files are located
	output: Test, train dataset
--------------------------------------------

4. FindDuplicateDataFiles.py:
	Creates a text file which contains all xls file names from given folder along with text from first row of each xls file	

	input: 
	file name for which duplicate has to be found
	folder path where the xls files exist

	output: text file
--------------------------------------------

5. CountNumberOfLines.py:
	Count total number of lines in english text files in a given folder
--------------------------------------------
6. SegreggateSentenceFromText.ipynb
Input: Text file having english text in paragraph style
Output: Another text file with single english sentence per line
Algorithm:
##Read the input file
##Split the text for '.' delimiter in a list
##Create new text file.
##Write each line from teh list to this text file

--------------------------------------------
7. SegreggateSentenceFromTextHindi.ipynb
Input: Text file having hindi text in paragraph style
Output: Another text file with single hindi sentence per line
Algorithm:
##Read the input file
##Split the text for '.' delimiter in a list
##Create new text file.
##Write each line from teh list to this text file

--------------------------------------------

8. EnglishHindiTranslation_V1.0.ipynb

input: Tatoeba challenge english-hindi dataset
output: outputs.zip

algorthm:
Get TatoebaChallenge.zip file and split to train and test(eval).
Save the train and test file as .tsv file
Use T5 model(T5Model("mt5", "google/mt5-small", args=model_args)) on the dataset
Finally get the output file

--------------------------------------------

9. MT5-FineTuning.ipynb -- incomplete

input: output.zip

--------------------------------------------

10. ConvertEnglishFullTextToHindi.ipynb

input:  English text file with each sentence in each line

algorthm:
Read each line and pass it to the function to translate
Get the translated output and writ it to another text file

--------------------------------------------

11. RunMt5_OnSadhguruData.ipynb

input: outputs.zip, consolidated english, hindi files translated files
output: translation for an english sentence
