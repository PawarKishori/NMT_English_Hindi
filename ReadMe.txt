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

